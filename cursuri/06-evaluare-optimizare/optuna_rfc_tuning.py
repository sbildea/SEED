#!/usr/bin/env python3
"""Optuna hyperparameter tuning for RandomForestClassifier.

This script runs an Optuna study to optimize meta-parameters of a
`sklearn.ensemble.RandomForestClassifier` using cross-validation on the
provided dataset. It then fits the best model on the training portion and
evaluates on a holdout test set.

By default the script persists Optuna trials to a local SQLite database so
you can inspect experiments in the Optuna dashboard. The trained model and
some metadata are saved with `joblib` for quick loading.

Usage example:
    python optuna_rfc_tuning.py --data ./date/Heart.csv --target AHD --trials 50 \
        --storage sqlite:///optuna_studies.db --study-name rfc_opt_study

Notes:
- The script performs simple preprocessing similar to the notebook: drops
    rows with missing values, maps common Yes/No targets to 1/0 and one-hot
    encodes `ChestPain` and `Thal` columns if present.
- The objective maximizes accuracy via StratifiedKFold cross-validation.
"""

import argparse
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from sklearn.metrics import accuracy_score
import optuna
import joblib


def load_and_preprocess(path, target_col):
    """Load CSV, drop missing rows and apply lightweight preprocessing.

    Parameters
    - path: path to a CSV file. The function skips the first column (index
      column) to match how the notebook loads the data.
    - target_col: name of the target column.

    Returns
    - X (pd.DataFrame): feature matrix
    - y (pd.Series): target vector
    """
    # read CSV and drop the first column (index) to match notebook behaviour
    df = pd.read_csv(path, header=0).iloc[:, 1:]
    # remove rows with any missing values
    df = df.dropna(how='any')

    # convert textual Yes/No-like targets to binary 1/0
    if df[target_col].dtype == object:
        df[target_col] = df[target_col].apply(
            lambda x: 1 if str(x).strip().lower() in ('yes', '1', 'true', 'y') else 0
        )

    # one-hot encode known categorical columns if present in dataset
    for col in ('ChestPain', 'Thal'):
        if col in df.columns:
            df = pd.get_dummies(df, columns=[col])

    X = df[[c for c in df.columns if c != target_col]]
    y = df[target_col]
    return X, y


def create_objective(X, y, random_state, cv_splits=5):
    """Create an Optuna objective function that evaluates RF by CV accuracy.

    The returned `objective` closure uses `cross_val_score` with
    `StratifiedKFold` to compute the mean accuracy for sampled hyperparameters.
    """
    skf = StratifiedKFold(n_splits=cv_splits, shuffle=True, random_state=random_state)

    def objective(trial):
        # sample common RandomForest hyperparameters
        n_estimators = trial.suggest_int('n_estimators', 50, 1000, log=True)
        max_depth = trial.suggest_int('max_depth', 2, 50)
        min_samples_split = trial.suggest_int('min_samples_split', 2, 20)
        min_samples_leaf = trial.suggest_int('min_samples_leaf', 1, 20)
        criterion = trial.suggest_categorical('criterion', ['gini', 'entropy'])
        bootstrap = trial.suggest_categorical('bootstrap', [True, False])

        # allow max_features as sqrt, log2 or a float fraction
        max_features_type = trial.suggest_categorical('max_features_type', ['sqrt', 'log2', 'float'])
        if max_features_type == 'float':
            max_features = trial.suggest_float('max_features_float', 0.1, 1.0)
        else:
            max_features = max_features_type

        # max_samples is only used when bootstrap=True
        max_samples = None
        if bootstrap:
            max_samples = trial.suggest_float('max_samples', 0.1, 1.0)

        clf = RandomForestClassifier(
            n_estimators=n_estimators,
            max_depth=max_depth,
            min_samples_split=min_samples_split,
            min_samples_leaf=min_samples_leaf,
            criterion=criterion,
            bootstrap=bootstrap,
            max_features=max_features,
            max_samples=max_samples,
            n_jobs=-1,
            random_state=random_state,
        )

        # run cross-validation and return mean accuracy (to maximize)
        scores = cross_val_score(clf, X, y, cv=skf, scoring='accuracy', n_jobs=1)
        return float(np.mean(scores))

    return objective


def run_study(data_path, target_col, trials, test_size, random_state, out_model_path, storage, study_name):
    """Run the Optuna study and save the resulting model + study object.

    Steps:
    1. Load and preprocess data
    2. Split into training and holdout test sets
    3. Optimize hyperparameters on the training set
    4. Refit best model on entire training set and evaluate on holdout
    5. Save model and study to `out_model_path`
    """
    # load data and create a holdout split
    X, y = load_and_preprocess(data_path, target_col)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, stratify=y, shuffle=True, random_state=random_state
    )

    # create and run the Optuna study (maximize accuracy)
    objective = create_objective(X_train, y_train, random_state)
    # use an RDB storage (SQLite) so trials are persisted and viewable via
    # the Optuna dashboard (e.g. `optuna-dashboard sqlite:///optuna_studies.db`).
    study = optuna.create_study(
        storage=storage,
        study_name=study_name,
        direction='maximize',
        load_if_exists=True,
    )
    study.optimize(objective, n_trials=trials, show_progress_bar=True)

    # show best trial info
    print('\nBest trial:')
    print('  Value: {}'.format(study.best_value))
    print('  Params:')
    for k, v in study.best_params.items():
        print('    {}: {}'.format(k, v))

    # Recreate best model and fit on full training set
    best_params = study.best_params.copy()
    # if a float max_features was sampled, rename the key to match sklearn
    if 'max_features_float' in best_params:
        best_params['max_features'] = best_params.pop('max_features_float')
    # if max_features_type is present and indicates a string option, use it
    if 'max_features_type' in best_params:
        if best_params['max_features_type'] in ('sqrt', 'log2'):
            best_params['max_features'] = best_params.pop('max_features_type')
        else:
            # if it was 'float' it was already converted above
            best_params.pop('max_features_type', None)

    # remove internal trial-only keys before constructing the classifier
    clf_init_args = {k: v for k, v in best_params.items() if k not in ('max_features_float',)}
    clf = RandomForestClassifier(**clf_init_args, n_jobs=-1, random_state=random_state)
    clf.fit(X_train, y_train)

    # evaluate on the holdout test set
    y_pred = clf.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print('\nTest accuracy on holdout set: {:.4f}'.format(acc))

    # persist both the trained model and the study for later analysis
    # Save only the trained model and basic metadata; the full trial history
    # is persisted in the SQLite storage specified with `--storage`.
    joblib.dump(
        {
            'model': clf,
            'best_params': study.best_params,
            'study_name': study.study_name,
            'storage': storage,
        },
        out_model_path,
    )
    print('\nSaved trained model and metadata to:', out_model_path)


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument('--data', type=str, default='./date/Heart.csv', help='Path to CSV file')
    p.add_argument('--target', type=str, default='AHD', help='Target column name')
    p.add_argument('--trials', type=int, default=50, help='Number of Optuna trials')
    p.add_argument('--test-size', type=float, default=0.3, help='Holdout test size')
    p.add_argument('--random-state', type=int, default=42, help='Random state')
    p.add_argument('--out', type=str, default='best_rfc_optuna.joblib', help='Output joblib path')
    p.add_argument('--storage', type=str, default='sqlite:///optuna_studies.db', help='Optuna RDB storage URL (e.g. sqlite:///optuna.db)')
    p.add_argument('--study-name', type=str, default='rfc_opt_study', help='Optuna study name')
    return p.parse_args()


if __name__ == '__main__':
    args = parse_args()
    run_study(args.data, args.target, args.trials, args.test_size, args.random_state, args.out, args.storage, args.study_name)

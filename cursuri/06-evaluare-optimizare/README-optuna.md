# Optuna tuning for RandomForestClassifier

This folder contains `optuna_rfc_tuning.py` — a small script that runs an
Optuna study to tune meta-parameters for `sklearn.ensemble.RandomForestClassifier`
on a dataset (the notebook uses `date/Heart.csv`). The script saves the best
trained model and the Optuna `Study` object as a joblib file.

Requirements
- Python 3.8+
- pandas
- numpy
- scikit-learn
- optuna
- joblib

Install with pip (recommended):

```bash
pip install pandas numpy scikit-learn optuna joblib
```

Or with conda:

```bash
conda install pandas numpy scikit-learn joblib -c conda-forge
pip install optuna
```

Quick usage

Run the tuning script from the repository root (example):

```bash
python optuna_rfc_tuning.py \
  --data ./date/Heart.csv \
  --target AHD \
  --trials 50 \
  --out best_rfc_optuna.joblib
```

Persisting trials to SQLite and viewing the dashboard

To persist Optuna trials in a local SQLite database so you can inspect them
with the Optuna dashboard, pass the `--storage` and `--study-name` options.
Example:

```bash
python optuna_rfc_tuning.py \
  --data ./date/Heart.csv \
  --target AHD \
  --trials 100 \
  --storage sqlite:///optuna_studies.db \
  --study-name rfc_opt_study
```

Then view the results with `optuna-dashboard` (install with `pip install optuna-dashboard`):

```bash
optuna-dashboard sqlite:///optuna_studies.db
# open http://127.0.0.1:8080 in a browser
```

Options
- `--data`: path to CSV file (default `./date/Heart.csv`)
- `--target`: target column name (default `AHD`)
- `--trials`: number of Optuna trials (default `50`)
- `--test-size`: holdout fraction for final evaluation (default `0.3`)
- `--out`: path to save model+study joblib (default `best_rfc_optuna.joblib`)

Notes
- The script performs light preprocessing (drops NA, maps Yes/No to 1/0,
  one-hot encodes `ChestPain` and `Thal` if present) to match the notebook
  workflow.
- Optuna can be interrupted and resumed if you persist the study database
  — the simple script uses an in-memory study by default.


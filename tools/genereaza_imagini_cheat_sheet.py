# Generează imaginile pentru cursuri/cheat-sheet-modelare.md (în cursuri/imagini-cheat-sheet/).
# Date sintetice, ca imaginile să nu depindă de seturile cursului. Rulare din rădăcina repository-ului:
#     python tools/genereaza_imagini_cheat_sheet.py
# Imaginile knn, arbore, random-forest, boosting, svm, kernel sunt extrase din curs-05b (atașamente).
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import FancyBboxPatch

DIR = os.path.join("cursuri", "imagini-cheat-sheet")
os.makedirs(DIR, exist_ok=True)

ALBASTRU, PORTOCALIU = "#2a6fbb", "#e8833a"          # aceleași culori ca imaginile din curs-05b
GRI, TEXT, TEXT2 = "#9d9d9d", "#222222", "#555555"
HARTA = LinearSegmentedColormap.from_list("ramane_pleaca", [ALBASTRU, "#f4f4f2", PORTOCALIU])
plt.rcParams.update({"font.size": 11, "axes.edgecolor": "#bbbbbb", "axes.labelcolor": TEXT,
                     "xtick.color": TEXT2, "ytick.color": TEXT2, "axes.titleweight": "bold",
                     "axes.spines.top": False, "axes.spines.right": False, "savefig.dpi": 150,
                     "savefig.bbox": "tight", "figure.facecolor": "white"})


def salveaza(fig, nume):
    fig.savefig(os.path.join(DIR, nume))
    plt.close(fig)
    print("scris:", nume)


def legenda_clase(fig, y=-0.02):
    h = [plt.Line2D([], [], marker="o", ls="", color=ALBASTRU, mec="white", ms=8, label="rămâne"),
         plt.Line2D([], [], marker="o", ls="", color=PORTOCALIU, mec="white", ms=8, label="pleacă")]
    fig.legend(handles=h, loc="lower center", ncol=2, frameon=False, bbox_to_anchor=(0.5, y))


# ---------------------------------------------------------------- 1. pașii unui model
def pasi_model():
    pasi = [("1", "Întrebarea,\nținta, metrica", "#e9eef6"), ("2", "Explorare\n(EDA)", "#e9eef6"),
            ("3", "Împărțire\ntrain / test", "#fde7d6"), ("4", "Pregătire\nîn Pipeline", "#e9eef6"),
            ("5", "Referință\n+ modele", "#e9eef6"), ("6", "Validare\nîncrucișată", "#e9eef6"),
            ("7", "Evaluare\npe test (o dată)", "#fde7d6"), ("8", "Concluzie\npentru client", "#e9eef6")]
    fig, ax = plt.subplots(figsize=(13, 3.4))
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 4)
    ax.axis("off")
    for i, (nr, txt, cul) in enumerate(pasi):
        x = 0.2 + i * 2
        ax.add_patch(FancyBboxPatch((x, 1.3), 1.6, 1.5, boxstyle="round,pad=0.05,rounding_size=0.15",
                                    fc=cul, ec="#8a8a8a", lw=1))
        ax.text(x + 0.8, 2.45, nr, ha="center", va="center", fontsize=13, weight="bold", color=TEXT)
        ax.text(x + 0.8, 1.8, txt, ha="center", va="center", fontsize=9.5, color=TEXT)
        if i < len(pasi) - 1:
            ax.annotate("", xy=(x + 1.95, 2.05), xytext=(x + 1.65, 2.05),
                        arrowprops=dict(arrowstyle="-|>", color=TEXT2, lw=1.2))
    # zona „învățat doar pe antrenare”
    ax.annotate("", xy=(11.8, 0.9), xytext=(6.2, 0.9), arrowprops=dict(arrowstyle="<->", color=ALBASTRU, lw=1.5))
    ax.text(9, 0.45, "tot ce se învață din date (imputare, scalare, one-hot, alpha, k...) se învață DOAR pe antrenare",
            ha="center", fontsize=9.5, color=ALBASTRU)
    ax.text(5, 3.4, "testul se pune deoparte aici...", ha="center", fontsize=9.5, color=PORTOCALIU)
    ax.text(13, 3.4, "...și se folosește o singură dată, aici", ha="center", fontsize=9.5, color=PORTOCALIU)
    ax.set_title("Pașii unui model, de la cerere la concluzie", fontsize=13, loc="left")
    salveaza(fig, "pasi-model.png")


# ---------------------------------------------------------------- 2. date sintetice 2D (vechime, cost lunar)
def date_2d(n=300, seed=1):
    rng = np.random.default_rng(seed)
    vechime = rng.uniform(0, 72, n)
    cost = rng.uniform(18, 120, n)
    z = -0.07 * vechime + 0.035 * cost - 1.0 + 1.2 * np.sin(vechime / 9)
    p = 1 / (1 + np.exp(-z))
    y = (rng.uniform(size=n) < p).astype(int)
    return np.c_[vechime, cost], y


# ---------------------------------------------------------------- 3. scalarea
def scalare():
    rng = np.random.default_rng(3)
    varsta = rng.normal(40, 10, 60)
    venit = rng.normal(5000, 1500, 60)
    fig, axs = plt.subplots(1, 2, figsize=(11, 4.2))
    # fără scalare: axe la aceeași unitate -> venitul domină
    ax = axs[0]
    ax.scatter(varsta, venit, s=22, color=ALBASTRU, ec="white", lw=0.5)
    ax.set_xlim(-2500, 2600)
    ax.set_aspect("equal")
    ax.set_xlabel("vârsta (ani)")
    ax.set_ylabel("venit (lei)")
    ax.set_title("Fără scalare, la aceeași unitate:\nvârsta e o linie, distanța = diferența de venit", fontsize=11)
    # cu scalare
    ax = axs[1]
    zv, zn = (varsta - varsta.mean()) / varsta.std(), (venit - venit.mean()) / venit.std()
    ax.scatter(zv, zn, s=22, color=ALBASTRU, ec="white", lw=0.5)
    ax.set_aspect("equal")
    ax.set_xlim(-3.2, 3.2)
    ax.set_ylim(-3.2, 3.2)
    ax.axhline(0, color="#dddddd", lw=0.8, zorder=0)
    ax.axvline(0, color="#dddddd", lw=0.8, zorder=0)
    ax.set_xlabel("vârsta standardizată (z)")
    ax.set_ylabel("venit standardizat (z)")
    ax.set_title("Cu standardizare (medie 0, abatere 1):\nambele coloane contează la fel", fontsize=11)
    salveaza(fig, "scalare.png")


# ---------------------------------------------------------------- 4. sigmoida și pragul
def sigmoida():
    rng = np.random.default_rng(0)
    x = rng.uniform(0, 72, 150)
    y = (rng.uniform(size=150) < 1 / (1 + np.exp(-(1.2 - 0.08 * x)))).astype(int)
    xs = np.linspace(-5, 100, 300)
    b = np.polyfit(x, y, 1)
    fig, ax = plt.subplots(figsize=(8, 4.2))
    ax.scatter(x, y + rng.normal(0, 0.015, 150), s=16, c=np.where(y == 1, PORTOCALIU, ALBASTRU), ec="white", lw=0.4, zorder=3)
    ax.plot(xs, np.polyval(b, xs), color=GRI, lw=2, ls="--")
    ax.plot(xs, 1 / (1 + np.exp(-(1.2 - 0.08 * xs))), color=TEXT, lw=2)
    ax.hlines(0.5, -8, 101, color=PORTOCALIU, lw=1, ls=":")
    ax.hlines(0.3, -8, 101, color=PORTOCALIU, lw=1, ls=":")
    ax.text(103, 0.5, "prag 0,5", va="center", fontsize=9, color=TEXT2)
    ax.text(103, 0.3, "prag 0,3", va="center", fontsize=9, color=TEXT2)
    ax.text(45, -0.27, "dreapta: iese sub 0 →", fontsize=9.5, color=TEXT2)
    ax.text(30, 0.55, "sigmoida: rămâne\nîntre 0 și 1", fontsize=9.5, color=TEXT)
    ax.set_ylim(-0.35, 1.15)
    ax.set_xlim(-8, 112)
    ax.set_xlabel("vechime (luni)")
    ax.set_ylabel("probabilitatea de plecare")
    ax.set_title("Regresia logistică: scor → probabilitate → clasă (după prag)", loc="left")
    salveaza(fig, "sigmoida.png")


# ---------------------------------------------------------------- 5. frontierele de decizie
def frontiere():
    from sklearn.pipeline import make_pipeline
    from sklearn.preprocessing import StandardScaler
    from sklearn.linear_model import LogisticRegression
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.ensemble import RandomForestClassifier, HistGradientBoostingClassifier
    from sklearn.svm import SVC
    X, y = date_2d()
    modele = [("Regresie logistică", make_pipeline(StandardScaler(), LogisticRegression())),
              ("kNN (k = 15)", make_pipeline(StandardScaler(), KNeighborsClassifier(15))),
              ("Arbore (max_depth = 4)", DecisionTreeClassifier(max_depth=4, random_state=0)),
              ("Random forest", RandomForestClassifier(300, min_samples_leaf=5, random_state=0)),
              ("Gradient boosting", HistGradientBoostingClassifier(max_depth=3, random_state=0)),
              ("SVM (kernel RBF)", make_pipeline(StandardScaler(), SVC(probability=True, random_state=0)))]
    descriere = ["o linie dreaptă", "petice după vecini", "dreptunghiuri (reguli)",
                 "dreptunghiuri netezite (vot)", "trepte fine (corecții)", "o curbă netedă"]
    xx, yy = np.meshgrid(np.linspace(0, 72, 200), np.linspace(18, 120, 200))
    grila = np.c_[xx.ravel(), yy.ravel()]
    fig, axs = plt.subplots(2, 3, figsize=(13, 8), sharex=True, sharey=True)
    for ax, (nume, m), d in zip(axs.ravel(), modele, descriere):
        m.fit(X, y)
        z = m.predict_proba(grila)[:, 1].reshape(xx.shape)
        ax.contourf(xx, yy, z, levels=np.linspace(0, 1, 11), cmap=HARTA, alpha=0.85)
        ax.contour(xx, yy, z, levels=[0.5], colors=TEXT, linewidths=1.2)
        ax.scatter(X[:, 0], X[:, 1], c=np.where(y == 1, PORTOCALIU, ALBASTRU), s=14, ec="white", lw=0.4)
        ax.set_title(f"{nume}\n{d}", fontsize=11)
    for ax in axs[1]:
        ax.set_xlabel("vechime (luni)")
    for ax in axs[:, 0]:
        ax.set_ylabel("cost lunar")
    fig.suptitle("Aceleași date, șase moduri de a trasa frontiera (linia neagră = probabilitate 0,5)",
                 fontsize=13, weight="bold", x=0.02, ha="left")
    legenda_clase(fig)
    fig.tight_layout(rect=(0, 0.03, 1, 0.97))
    salveaza(fig, "frontiere.png")


# ---------------------------------------------------------------- 6. Ridge vs Lasso
def regularizare():
    from sklearn.datasets import make_regression
    from sklearn.linear_model import Ridge, Lasso
    from sklearn.preprocessing import StandardScaler
    X, y = make_regression(200, 8, n_informative=4, noise=20, random_state=2)
    X = StandardScaler().fit_transform(X)
    alfe = np.logspace(-2, 4, 60)
    fig, axs = plt.subplots(1, 2, figsize=(12, 4.2), sharey=True)
    for ax, (nume, M, a) in zip(axs, [("Ridge: coeficienții scad, dar nu ajung la 0", Ridge, alfe),
                                      ("Lasso: coeficienții se anulează pe rând", Lasso, alfe / 20)]):
        coef = np.array([M(alpha=v, max_iter=20000).fit(X, y).coef_ for v in a])
        for j in range(coef.shape[1]):
            ax.plot(a, coef[:, j], lw=2, color=ALBASTRU if j % 2 == 0 else PORTOCALIU)
        ax.axhline(0, color=GRI, lw=0.8)
        ax.set_xscale("log")
        ax.set_xlabel("alpha (cât de tare penalizăm) →")
        ax.set_title(nume, fontsize=11)
    axs[0].set_ylabel("coeficient (date standardizate)")
    fig.suptitle("Regularizarea ține coeficienții în frâu; alpha se alege prin validare încrucișată",
                 fontsize=12, weight="bold", x=0.02, ha="left")
    fig.tight_layout()
    salveaza(fig, "regularizare.png")


# ---------------------------------------------------------------- 7. sub/supraînvățare
def complexitate():
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.model_selection import train_test_split
    X, y = date_2d(n=600, seed=4)
    Xa, Xt, ya, yt = train_test_split(X, y, test_size=0.3, stratify=y, random_state=42)
    ad = range(1, 16)
    sa, st = [], []
    for d in ad:
        m = DecisionTreeClassifier(max_depth=d, random_state=0).fit(Xa, ya)
        sa.append(m.score(Xa, ya))
        st.append(m.score(Xt, yt))
    best = list(ad)[int(np.argmax(st))]
    fig, ax = plt.subplots(figsize=(8, 4.2))
    ax.plot(ad, sa, color=ALBASTRU, lw=2, marker="o", ms=5)
    ax.plot(ad, st, color=PORTOCALIU, lw=2, marker="o", ms=5)
    ax.text(15.3, sa[-1], "antrenare", va="center", color=TEXT, fontsize=10)
    ax.text(15.3, st[-1], "test", va="center", color=TEXT, fontsize=10)
    ax.axvline(best, color=GRI, ls=":", lw=1)
    ax.text(0.7, st[0] - 0.02, "subînvățare:\nprea simplu", fontsize=9.5, color=TEXT2, va="top")
    ax.text(10, (sa[-1] + st[-1]) / 2, "supraînvățare:\nmemorează", fontsize=9.5, color=TEXT2, ha="center")
    ax.text(best + 0.2, max(sa) - 0.01, f"echilibru\n(max_depth ≈ {best})", fontsize=9.5, color=TEXT2, va="top")
    ax.set_xlim(0.5, 16.8)
    ax.set_xlabel("complexitatea modelului (adâncimea arborelui)")
    ax.set_ylabel("acuratețe")
    ax.set_title("Distanța dintre antrenare și test arată supraînvățarea", loc="left")
    salveaza(fig, "complexitate.png")


# ---------------------------------------------------------------- 8. validarea încrucișată
def validare_incrucisata():
    fig, ax = plt.subplots(figsize=(11, 3.8))
    ax.set_xlim(0, 12)
    ax.set_ylim(-0.6, 6)
    ax.axis("off")
    for r in range(5):
        yv = 4.6 - r
        for k in range(5):
            val = k == r
            ax.add_patch(FancyBboxPatch((0.2 + k * 1.75, yv), 1.65, 0.7, boxstyle="round,pad=0.02,rounding_size=0.08",
                                        fc=PORTOCALIU if val else "#d7e3f2", ec="white", lw=2))
            ax.text(1.02 + k * 1.75, yv + 0.35, "validare" if val else "antrenare", ha="center", va="center",
                    fontsize=9, color="white" if val else TEXT)
        ax.text(9.1, yv + 0.35, f"runda {r + 1} → scor {r + 1}", va="center", fontsize=9.5, color=TEXT)
    ax.add_patch(FancyBboxPatch((10.75, 0.6), 1.1, 4.7, boxstyle="round,pad=0.02,rounding_size=0.08",
                                fc="#e3e3e3", ec="white", lw=2))
    ax.text(11.3, 2.95, "TEST\n(pus\ndeoparte,\nneatins)", ha="center", va="center", fontsize=9.5, color=TEXT)
    ax.text(0.2, -0.25, "rezultat = media celor 5 scoruri ± abaterea lor → un interval, nu o singură cifră norocoasă",
            fontsize=10, color=TEXT)
    ax.text(0.2, 5.55, "Partea de ANTRENARE e împărțită în 5 părți (folds)", fontsize=12, weight="bold", color=TEXT)
    salveaza(fig, "validare-incrucisata.png")


# ---------------------------------------------------------------- 9. grid search vs Optuna
def grid_vs_optuna():
    import optuna
    optuna.logging.set_verbosity(optuna.logging.WARNING)

    def scor(lc, lg):                     # o „suprafață de scor” inventată, cu vârful în colț
        return 0.85 * np.exp(-((lc - 1.3) ** 2) / 1.6 - ((lg + 2.4) ** 2) / 0.5) + 0.05 * np.cos(2 * lc)

    lc, lg = np.meshgrid(np.linspace(-2, 3, 200), np.linspace(-4, 1, 200))
    fig, axs = plt.subplots(1, 2, figsize=(12, 4.8), sharey=True)
    for ax, titlu in zip(axs, ["Grid search: 5 × 5 = 25 de încercări,\ntoate combinațiile, la distanțe egale",
                               "Optuna: tot 25 de încercări,\nse concentrează unde scorul e mare"]):
        cs = ax.contourf(lc, lg, scor(lc, lg), levels=12, cmap="Blues", alpha=0.85)
        ax.set_title(titlu, fontsize=11)
        ax.set_xlabel("log10(C)")
    axs[0].set_ylabel("log10(gamma)")
    g1, g2 = np.meshgrid(np.linspace(-2, 3, 5), np.linspace(-4, 1, 5))
    axs[0].scatter(g1, g2, s=46, color=PORTOCALIU, ec="white", lw=1, zorder=3)
    studiu = optuna.create_study(direction="maximize", sampler=optuna.samplers.TPESampler(seed=0))
    studiu.optimize(lambda t: scor(t.suggest_float("lc", -2, 3), t.suggest_float("lg", -4, 1)), n_trials=25)
    pts = np.array([[t.params["lc"], t.params["lg"]] for t in studiu.trials])
    axs[1].scatter(pts[:10, 0], pts[:10, 1], s=46, color="white", ec=PORTOCALIU, lw=1.5, zorder=3, label="primele 10 (explorare)")
    axs[1].scatter(pts[10:, 0], pts[10:, 1], s=46, color=PORTOCALIU, ec="white", lw=1, zorder=3, label="următoarele 15 (exploatare)")
    axs[1].legend(loc="upper center", bbox_to_anchor=(0.5, -0.15), ncol=2, fontsize=9, frameon=False)
    cb = fig.colorbar(cs, ax=axs, shrink=0.85, pad=0.02)
    cb.set_label("scor în validarea încrucișată")
    salveaza(fig, "grid-vs-optuna.png")


# ---------------------------------------------------------------- 10. pragul ales după profit (lab-set1, ca în curs-06)
def profit_prag():
    import sys
    import pandas as pd
    sys.path.insert(0, os.path.abspath("."))
    from seed.date import incarca
    from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_predict
    from sklearn.compose import make_column_transformer, make_column_selector
    from sklearn.preprocessing import OneHotEncoder, StandardScaler
    from sklearn.pipeline import make_pipeline
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import confusion_matrix
    df = incarca("lab-set1")[0]
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce").fillna(0)
    y = (df["Churn"] == "Yes").astype(int)
    X = df.drop(columns=["customerID", "Churn"])
    X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, stratify=y, random_state=17)
    model = make_pipeline(make_column_transformer(
        (StandardScaler(), make_column_selector(dtype_include="number")),
        (OneHotEncoder(handle_unknown="ignore"), make_column_selector(dtype_exclude="number"))),
        LogisticRegression(max_iter=1000))
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=17)
    p = cross_val_predict(model, X_train, y_train, cv=cv, method="predict_proba")[:, 1]
    praguri = np.round(np.arange(0.05, 0.96, 0.05), 2)
    profit = []
    for prag in praguri:
        tn, fp, fn, tp = confusion_matrix(y_train, (p >= prag).astype(int)).ravel()
        profit.append((tp * 250 - fp * 50) / 1000)
    best = praguri[int(np.argmax(profit))]
    i05 = int(np.where(praguri == 0.5)[0][0])
    fig, ax = plt.subplots(figsize=(8, 4.2))
    ax.plot(praguri, profit, color=ALBASTRU, lw=2, marker="o", ms=5)
    ax.axvline(0.5, color=GRI, ls="--", lw=1)
    ax.axvline(best, color=PORTOCALIU, lw=1.5)
    ax.text(0.51, profit[i05] + 6, f"prag implicit 0,5\n{profit[i05]:.0f} mii lei", fontsize=9.5, color=TEXT2)
    ax.text(best + 0.01, max(profit) + 2, f"prag cu profit maxim {best:.2f}".replace(".", ",") + f"\n{max(profit):.0f} mii lei", fontsize=9.5,
            color=TEXT, va="bottom")
    ax.set_ylim(min(profit) - 5, max(profit) * 1.25)
    ax.set_xlabel("pragul de probabilitate peste care trimitem oferta")
    ax.set_ylabel("profit estimat (mii lei)")
    ax.set_title("Pragul se alege din bani, pe validarea încrucișată (Telco, antrenare)", loc="left", fontsize=11.5)
    salveaza(fig, "profit-prag.png")


if __name__ == "__main__":
    profit_prag()
    pasi_model()
    scalare()
    sigmoida()
    frontiere()
    regularizare()
    complexitate()
    validare_incrucisata()
    grid_vs_optuna()

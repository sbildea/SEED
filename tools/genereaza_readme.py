"""Regenerează tabelul cu programa din README.md pe baza folderelor din cursuri/.

Folosire:  python tools/genereaza_readme.py
Tabelul se scrie între marcajele <!-- PROGRAMA --> și <!-- /PROGRAMA --> din README.md;
restul README-ului rămâne neschimbat. Titlurile modulelor se modifică în TITLURI.
Materialele `extra-*` nu apar în tabel; sunt listate în README.md-ul fiecărui modul.
"""

import re
import sys
from pathlib import Path

RADACINA = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RADACINA))
from seed.catalog import GITHUB_USER, REPO  # noqa: E402

TITLURI = {
    "01-date-intrebari-ai": "Date, întrebări și lucrul cu AI",
    "02-explorare-vizualizare": "Analiza exploratorie și vizualizarea datelor",
    "03-invatare-nesupervizata": "Învățare nesupervizată: PCA, clusterizare, asociere",
    "04-regresie": "Regresie: modele liniare, supraînvățare, regularizare",
    "05-clasificare": "Clasificare: regresie logistică, arbori, ansambluri, SVM",
    "06-evaluare-optimizare": "Evaluare și optimizare: metrici, validare încrucișată, Optuna",
    "07-proiect": "Proiect: de la întrebare la decizie",
}
BADGE = "https://colab.research.google.com/assets/colab-badge.svg"


def eticheta(f):
    rest = re.sub(r"^(curs|seminar|tema|extra)-\d+[a-z]?-", "", f.stem)
    return rest.replace("-", " ").capitalize()


def link_nb(rel, f):
    colab = f"https://colab.research.google.com/github/{GITHUB_USER}/{REPO}/blob/main/{rel}/{f.name}"
    return f"[![Colab]({BADGE})]({colab}) [{eticheta(f)}]({rel}/{f.name})"


def celula(folder, rel, prefix):
    pdfuri = [f"[{eticheta(f)}]({rel}/{f.name}) (PDF)" for f in sorted(folder.glob(f"{prefix}-*.pdf"))]
    nbs = [link_nb(rel, f) for f in sorted(folder.glob(f"{prefix}-*.ipynb"))]
    return "<br>".join(pdfuri + nbs) or "-"


def tabel():
    randuri = ["| Modul | Curs (2h) | Seminar (2h) | Temă |", "|---|---|---|---|"]
    for folder in sorted((RADACINA / "cursuri").iterdir()):
        if not folder.is_dir():
            continue
        rel = f"cursuri/{folder.name}"
        titlu = f"**{int(folder.name[:2])}.** [{TITLURI.get(folder.name, folder.name)}]({rel})"
        tema = celula(folder, rel, "tema")
        if folder.name == "07-proiect":
            tema = f"[Descrierea proiectelor]({rel}/descriere-proiecte.ipynb)"
        randuri.append(f"| {titlu} | {celula(folder, rel, 'curs')} | {celula(folder, rel, 'seminar')} | {tema} |")
    return "\n".join(randuri)


def main():
    sys.stdout.reconfigure(encoding="utf-8")  # diacriticele în consola Windows
    sys.stderr.reconfigure(encoding="utf-8")
    if sys.argv[1:]:
        sys.exit(__doc__)
    readme = RADACINA / "README.md"
    text = readme.read_text(encoding="utf-8")
    nou = re.sub(r"(<!-- PROGRAMA -->).*?(<!-- /PROGRAMA -->)",
                 lambda m: m.group(1) + "\n" + tabel() + "\n" + m.group(2), text, flags=re.S)
    readme.write_text(nou, encoding="utf-8")
    print("README.md actualizat")


if __name__ == "__main__":
    main()

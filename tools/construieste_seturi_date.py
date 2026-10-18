"""Construiește arhivele ZIP ale seturilor de date, gata de atașat la release-ul GitHub.

Folosire (în PowerShell, din C:\\UNITBV\\SEED; toate cele trei căi sunt obligatorii):
    python tools/construieste_seturi_date.py `
        --seturi    "C:\\Users\\User\\OneDrive\\work\\UNITBV\\SETURI_DE_DATE" `
        --date-curs "C:\\Users\\User\\OneDrive\\work\\UNITBV\\2026-2027\\SEM I\\ADS1\\date.zip" `
        --iesire    "C:\\Users\\User\\OneDrive\\work\\UNITBV\\2026-2027\\SEM I\\SEED_extras\\release-assets"

Rezultatul conține câte un <nume>.zip pentru fiecare set din seed/catalog.py.
Arhivele se încarcă pe GitHub la Releases -> tag `date-v1`. Vezi docs/ghid-profesor.md, secțiunea 2.
"""

import argparse
import sys
import urllib.request
import zipfile
from pathlib import Path

RADACINA = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RADACINA))
from seed.catalog import CATALOG  # noqa: E402

# fișiere suplimentare (nu sunt tabele) incluse în arhivele de laborator
EXTRA_LAB = {"lab-set6": ["data_description.txt"]}

# în DateProiecte.zip arhivele 04 și 16 conțin alte date decât cele din descrierea proiectelor
# (16 este o copie a lui 18); acestea se descarcă direct de pe Kaggle (seturi publice)
DIN_KAGGLE = {
    "proiect-04": "https://www.kaggle.com/api/v1/datasets/download/aljarah/xAPI-Edu-Data",
    "proiect-16": "https://www.kaggle.com/api/v1/datasets/download/fedesoriano/spanish-wine-quality-dataset",
}


def scrie_zip(iesire, nume, intrari):
    """intrari: listă de (nume_in_arhiva, bytes)."""
    cale = iesire / f"{nume}.zip"
    with zipfile.ZipFile(cale, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as zf:
        for arcname, date in intrari:
            zf.writestr(arcname, date)
    print(f"{nume:<11} {cale.stat().st_size / 2**20:8.1f} MB")


def seturi_laborator(sursa, iesire):
    with zipfile.ZipFile(sursa / "DateLaborator.zip") as zf:
        for nume, info in CATALOG.items():
            if not nume.startswith("lab-"):
                continue
            folder = "DateLaborator/Kaggle/Set" + nume.removeprefix("lab-set")
            fisiere = info["fisiere"] + EXTRA_LAB.get(nume, [])
            scrie_zip(iesire, nume, [(f, zf.read(f"{folder}/{f}")) for f in fisiere])


def seturi_proiecte(sursa, iesire):
    with zipfile.ZipFile(sursa / "DateProiecte.zip") as zf:
        for nume in CATALOG:
            if nume.startswith("proiect-"):
                nr = nume.removeprefix("proiect-")
                if nume in DIN_KAGGLE:
                    date = urllib.request.urlopen(DIN_KAGGLE[nume]).read()
                else:
                    date = zf.read(f"SeturiDeDate/set_date_tema_proiect_nr{nr}.zip")
                (iesire / f"{nume}.zip").write_bytes(date)
                print(f"{nume:<11} {len(date) / 2**20:8.1f} MB")


def set_date_curs(date_zip, iesire):
    with zipfile.ZipFile(date_zip) as zf:
        intrari = [(i.filename.removeprefix("date/"), zf.read(i)) for i in zf.infolist()
                   if not i.is_dir()]
    scrie_zip(iesire, "date-curs", intrari)


def main():
    sys.stdout.reconfigure(encoding="utf-8")  # diacriticele în consola Windows
    sys.stderr.reconfigure(encoding="utf-8")
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--seturi", type=Path, required=True,
                   help="folderul SETURI_DE_DATE (cu DateLaborator.zip și DateProiecte.zip)")
    p.add_argument("--date-curs", type=Path, required=True,
                   help="arhiva date.zip cu folderele csv/, xlsx/, json/ folosite la curs")
    p.add_argument("--iesire", type=Path, required=True,
                   help="folderul unde se scriu arhivele (SEED_extras/release-assets din OneDrive)")
    a = p.parse_args()
    a.iesire.mkdir(parents=True, exist_ok=True)
    set_date_curs(a.date_curs, a.iesire)
    seturi_laborator(a.seturi, a.iesire)
    seturi_proiecte(a.seturi, a.iesire)


if __name__ == "__main__":
    main()

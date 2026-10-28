"""Încărcarea seturilor de date ale cursului SEED, la fel în Colab și local.

    from seed.date import incarca
    date = incarca("lab-set4")       # toate tabelele setului
    df = date["OnlineRetail"]         # un tabel după nume...
    df = date[0]                      # ...sau după poziție
    df = incarca("lab-set5", "credit_train")   # direct un singur tabel

La prima folosire, arhiva setului se descarcă din release-ul GitHub al cursului
și se dezarhivează într-un folder local; apoi se citește de acolo.
"""

import difflib
import os
import shutil
import sqlite3
import sys
import urllib.request
import zipfile
from pathlib import Path

import pandas as pd

from .catalog import CATALOG, GITHUB_USER, REPO, TAG_DATE

URL_DATE = "https://github.com/{user}/{repo}/releases/download/{tag}/{nume}.zip"
EXTENSII = {".csv", ".xlsx", ".xls", ".json", ".sqlite", ".db", ".zip"}


def _folder_cache():
    if os.environ.get("SEED_DATE_CACHE"):
        return Path(os.environ["SEED_DATE_CACHE"])
    if "google.colab" in sys.modules:
        return Path("/content/seed_date")
    return Path.home() / ".seed_date"


def _verifica_nume(nume):
    if nume not in CATALOG:
        apropiate = difflib.get_close_matches(nume, CATALOG, n=3)
        sugestie = f" Poate ați vrut: {', '.join(apropiate)}?" if apropiate else ""
        raise ValueError(f"Setul de date '{nume}' nu există.{sugestie} "
                         "Lista completă: lista_seturi()")


def _aduce_arhiva(nume, destinatie):
    """Copiază arhiva dintr-un folder local (SEED_DATE_LOCAL) sau o descarcă de pe GitHub."""
    local = os.environ.get("SEED_DATE_LOCAL")
    if local and (Path(local) / f"{nume}.zip").exists():
        shutil.copy(Path(local) / f"{nume}.zip", destinatie)
        return
    url = URL_DATE.format(user=GITHUB_USER, repo=REPO, tag=TAG_DATE, nume=nume)
    print(f"Descărcare {nume} (doar prima dată)...")
    urllib.request.urlretrieve(url, destinatie)


def descarca(nume):
    """Aduce setul de date local (o singură dată) și întoarce folderul cu fișierele lui."""
    _verifica_nume(nume)
    folder = _folder_cache() / nume
    if (folder / ".gata").exists():
        return folder
    folder.mkdir(parents=True, exist_ok=True)
    arhiva = folder.with_suffix(".zip")
    _aduce_arhiva(nume, arhiva)
    with zipfile.ZipFile(arhiva) as zf:
        zf.extractall(folder)
    arhiva.unlink()
    (folder / ".gata").touch()
    return folder


class SetDate(dict):
    """Dicționar nume_tabel -> DataFrame care acceptă și poziția: date[0]."""

    def __getitem__(self, cheie):
        if isinstance(cheie, int):
            return list(self.values())[cheie]
        return super().__getitem__(cheie)

    def __repr__(self):
        randuri = [f"  [{i}] {nume}: {df.shape[0]} rânduri x {df.shape[1]} coloane"
                   for i, (nume, df) in enumerate(self.items())]
        return "SetDate cu tabelele:\n" + "\n".join(randuri)


def _citeste_csv(cale):
    try:
        return pd.read_csv(cale, low_memory=False)
    except UnicodeDecodeError:
        return pd.read_csv(cale, low_memory=False, encoding="latin-1")


def _citeste_sqlite(cale, tabel):
    with sqlite3.connect(cale) as conn:
        return pd.read_sql_query(f'SELECT * FROM "{tabel}"', conn)


def _index_tabele(nume, folder):
    """Întoarce {nume_tabel: funcție_de_citire}, în ordinea din catalog."""
    ordine = CATALOG[nume].get("fisiere", [])
    gasite = [f for f in folder.rglob("*") if f.is_file() and f.suffix.lower() in EXTENSII]
    gasite.sort(key=lambda f: (ordine.index(f.name) if f.name in ordine else len(ordine), str(f)))
    stems = [f.stem for f in gasite]

    index = {}
    for f in gasite:
        cheie = f.stem if stems.count(f.stem) == 1 else f.relative_to(folder).with_suffix("").as_posix()
        ext = f.suffix.lower()
        if ext == ".csv":
            index[cheie] = lambda f=f: _citeste_csv(f)
        elif ext in (".xlsx", ".xls"):
            index[cheie] = lambda f=f: pd.read_excel(f)
        elif ext == ".json":
            index[cheie] = lambda f=f: pd.read_json(f)
        elif ext == ".zip":
            index[cheie] = lambda f=f: pd.read_json(f, compression="zip")
        else:  # baze de date SQLite: câte o intrare pentru fiecare tabel
            with sqlite3.connect(f) as conn:
                tabele = [r[0] for r in conn.execute(
                    "SELECT name FROM sqlite_master WHERE type='table' "
                    "AND name NOT LIKE 'sqlite_%' ORDER BY name")]
            for t in tabele:
                index[t] = lambda f=f, t=t: _citeste_sqlite(f, t)
    return index


def incarca(nume, tabel=None):
    """Încarcă un set de date din catalog.

    nume:  numele setului, de exemplu "lab-set4" sau "proiect-07" (vezi lista_seturi()).
    tabel: opțional, numele sau poziția unui singur tabel; altfel se încarcă toate.
    """
    index = _index_tabele(nume, descarca(nume))
    if tabel is None:
        return SetDate((cheie, citeste()) for cheie, citeste in index.items())
    chei = list(index)
    if isinstance(tabel, int):
        return index[chei[tabel]]()
    if tabel not in index:
        raise KeyError(f"Tabelul '{tabel}' nu există în {nume}. Tabele disponibile: {chei}")
    return index[tabel]()


def lista_seturi(filtru=""):
    """Afișează seturile de date disponibile (opțional doar cele care încep cu `filtru`)."""
    for nume, info in CATALOG.items():
        if nume.startswith(filtru):
            print(f"{nume:<11} {info['titlu']}")

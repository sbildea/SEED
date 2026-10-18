"""Descarcă dinainte seturile de date, ca laboratoarele să meargă și fără internet.

Folosire (din folderul SEED, cu mediul activat):
    python tools/descarca_seturi.py            # seturile de curs și de laborator (~120 MB)
    python tools/descarca_seturi.py proiect-07 # doar anumite seturi
    python tools/descarca_seturi.py --toate    # tot catalogul, inclusiv proiectele (~250 MB)

Seturile ajung în folderul cache (implicit ~/.seed_date); după aceea incarca(...) nu mai
are nevoie de internet.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from seed.catalog import CATALOG  # noqa: E402
from seed.date import descarca  # noqa: E402


def main():
    sys.stdout.reconfigure(encoding="utf-8")  # diacriticele în consola Windows
    sys.stderr.reconfigure(encoding="utf-8")
    necunoscute = [a for a in sys.argv[1:] if a != "--toate" and a not in CATALOG]
    if necunoscute:
        sys.exit(__doc__ + "\nSeturi necunoscute: " + ", ".join(necunoscute))
    argumente = sys.argv[1:]
    if "--toate" in argumente:
        nume = list(CATALOG)
    elif argumente:
        nume = argumente
    else:
        nume = [n for n in CATALOG if not n.startswith("proiect-")]
    for n in nume:
        print(f"{n:<11} -> {descarca(n)}")
    print("Gata: aceste seturi pot fi încărcate acum și fără internet.")


if __name__ == "__main__":
    main()

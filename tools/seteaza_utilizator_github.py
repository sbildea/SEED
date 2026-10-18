"""Înlocuiește numele de utilizator GitHub în tot repository-ul (link-uri Colab, imagini, date).

Folosire:  python tools/seteaza_utilizator_github.py <utilizator-nou> [<utilizator-vechi>]
Implicit, utilizatorul vechi este YOUR-USERNAME (valoarea de pornire).
"""

import sys
from pathlib import Path

RADACINA = Path(__file__).resolve().parents[1]
EXTENSII = {".ipynb", ".md", ".py", ".txt", ".yml", ".html"}


def main():
    sys.stdout.reconfigure(encoding="utf-8")  # diacriticele în consola Windows
    sys.stderr.reconfigure(encoding="utf-8")
    if len(sys.argv) not in (2, 3) or any(a.startswith("-") for a in sys.argv[1:]):
        sys.exit(__doc__)
    nou = sys.argv[1]
    vechi = sys.argv[2] if len(sys.argv) == 3 else "YOUR-USERNAME"
    for f in RADACINA.rglob("*"):
        if f.suffix not in EXTENSII or ".git" in f.parts or f.resolve() == Path(__file__).resolve():
            continue
        text = f.read_text(encoding="utf-8")
        if vechi in text:
            f.write_text(text.replace(vechi, nou), encoding="utf-8", newline="")
            print("actualizat:", f.relative_to(RADACINA))


if __name__ == "__main__":
    main()

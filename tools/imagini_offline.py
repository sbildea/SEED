"""Face imaginile din notebook-uri să se vadă și fără internet, într-o copie locală a cursului.

Notebook-urile folosesc adrese GitHub pentru imagini, pentru că doar așa se văd în Colab.
Acest script le înlocuiește, în copia ta locală, cu căi relative către fișierele din repository.

Folosire (din folderul SEED):
    python tools/imagini_offline.py            # trece pe imagini locale
    python tools/imagini_offline.py --online   # revine la adresele GitHub
"""

import os
import re
import sys
from pathlib import Path

RADACINA = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RADACINA))
from seed.catalog import GITHUB_USER, REPO  # noqa: E402

RAW = f"https://raw.githubusercontent.com/{GITHUB_USER}/{REPO}/main/"


def main():
    sys.stdout.reconfigure(encoding="utf-8")  # diacriticele în consola Windows
    sys.stderr.reconfigure(encoding="utf-8")
    if sys.argv[1:] not in ([], ["--online"]):
        sys.exit(__doc__)
    online = "--online" in sys.argv
    for nb in RADACINA.rglob("*.ipynb"):
        if ".ipynb_checkpoints" in nb.parts:
            continue
        text = nb.read_text(encoding="utf-8")
        prefix = os.path.relpath(RADACINA, nb.parent).replace(os.sep, "/") + "/"
        if online:
            nou = re.sub(r'(src=\\"|\]\()' + re.escape(prefix), lambda m: m.group(1) + RAW, text)
        else:
            nou = text.replace(RAW, prefix)
        if nou != text:
            nb.write_text(nou, encoding="utf-8", newline="")
            print("actualizat:", nb.relative_to(RADACINA))


if __name__ == "__main__":
    main()

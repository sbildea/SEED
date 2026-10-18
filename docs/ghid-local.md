# Ghid: lucrul local, pe calculatorul tău (și fără internet)

Varianta locală este utilă când internetul din laborator este instabil: după o pregătire făcută o singură dată (cu internet), notebook-urile, datele și imaginile funcționează **complet offline**. Pentru varianta din browser vezi [ghidul Colab](ghid-colab.md).

Pregătirea durează 15-20 de minute. Fă-o acasă, înainte de primul laborator.

## 1. Instalează Python

**Windows**

1. Descarcă Python **3.12** de la <https://www.python.org/downloads/windows/> („Windows installer (64-bit)").
2. În primul ecran al instalatorului bifează **Add python.exe to PATH**, apoi **Install Now**.
3. Verifică: deschide **PowerShell** și scrie `python --version`. Trebuie să apară `Python 3.12.x`.

(Alternativ, din PowerShell: `winget install Python.Python.3.12`.)

**macOS:** instalează Python 3.12 de pe python.org sau cu `brew install python@3.12`; în comenzile de mai jos folosește `python3` în loc de `python`.

## 2. Instalează VS Code (editorul)

1. Descarcă de la <https://code.visualstudio.com/> și instalează.
2. Deschide VS Code → **Extensions** (Ctrl+Shift+X) → instalează **Python** și **Jupyter** (ambele de la Microsoft).

## 3. Descarcă materialele cursului

**Varianta A, cu Git (recomandată, actualizările se iau cu o comandă):**

```
git clone https://github.com/prof/SEED.git
```

(Git se instalează de la <https://git-scm.com/downloads>; sau folosește GitHub Desktop: File → Clone repository.)

**Varianta B, fără Git:** pe pagina cursului apasă **Code → Download ZIP** și dezarhivează într-un folder, de exemplu `Documente\SEED`.

## 4. Creează mediul Python al cursului

Deschide folderul `SEED` în VS Code (**File → Open Folder**), apoi deschide un terminal (**Terminal → New Terminal**) și rulează:

**Windows (PowerShell):**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements-local.txt
```

> Dacă PowerShell refuză activarea („running scripts is disabled"), rulează o dată
> `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`, confirmă cu `Y`, apoi reia activarea.

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-local.txt
```

Când mediul este activ, linia de comandă începe cu `(.venv)`. Mai simplu, pe Windows poți rula totul dintr-o comandă: `.\tools\creeaza_mediu_local.ps1`.

## 5. Pregătește lucrul fără internet

Tot din terminalul cu `(.venv)` activ:

```
python tools/descarca_seturi.py
python tools/imagini_offline.py
```

- Prima comandă descarcă seturile de date de curs și de laborator (~120 MB). Pentru proiect adaugă numărul tău, de exemplu `python tools/descarca_seturi.py proiect-07`, sau `--toate` pentru tot.
- A doua face ca imaginile din notebook-uri să se încarce din folderul cursului, nu de pe internet.

## 6. Deschide și rulează un notebook

1. În VS Code, deschide un notebook din `cursuri/...` (de exemplu `cursuri/02-explorare-vizualizare/seminar-02-explorare-vizualizare.ipynb`).
2. Sus-dreapta, **Select Kernel → Python Environments → .venv**.
3. Rulează prima celulă, **Configurare curs** (local nu descarcă nimic; doar face pachetul cursului vizibil), apoi celelalte cu **Shift + Enter**.
4. Datele se încarcă la fel ca în Colab:

   ```python
   from seed.date import incarca
   date = incarca("lab-set4")
   df = date[0]
   ```

Lucrează pe o copie a temei (de exemplu `tema-02-NumePrenume.ipynb`), ca actualizările cursului să nu intre în conflict cu rezolvarea ta.

## 7. Actualizări

- **Cu Git:** în folderul `SEED` rulează `git pull`. Dacă ai rulat `imagini_offline.py`, rulează înainte `python tools/imagini_offline.py --online`, apoi din nou fără `--online` după actualizare. Dacă `requirements.txt` s-a schimbat, rulează iar `pip install -r requirements-local.txt`.
- **Fără Git:** descarcă din nou ZIP-ul și copiază-ți temele în noul folder.

## Probleme frecvente

| Problemă | Soluție |
| --- | --- |
| `python` nu este recunoscut | Python nu e în PATH: reinstalează bifând **Add python.exe to PATH**, apoi redeschide terminalul. |
| `ModuleNotFoundError: No module named 'seed'` | Notebook-ul nu rulează din folderul lui sau nu ai rulat celula **Configurare curs**. Deschide-l din `cursuri/...` și rulează prima celulă. |
| `ModuleNotFoundError` pentru alt pachet | Kernelul selectat nu este `.venv`. Alege-l din **Select Kernel**, sau rulează din nou `pip install -r requirements-local.txt` cu mediul activ. |
| `incarca` încearcă să descarce și nu are internet | Setul nu a fost descărcat la pasul 5. Rulează `python tools/descarca_seturi.py <nume-set>` când ai internet. |
| Imaginile din notebook nu apar | Rulează `python tools/imagini_offline.py`. |
| VS Code nu vede mediul `.venv` | **Ctrl+Shift+P → Python: Select Interpreter** → alege cel din `.venv`, apoi repornește VS Code. |

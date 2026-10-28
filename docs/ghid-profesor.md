# Ghid pentru profesor: publicare și actualizare

## 0. Unde stau fișierele (lucrul pe mai multe calculatoare)

| Ce | Unde | Cum se sincronizează |
| --- | --- | --- |
| Repository-ul `SEED` | `C:\UNITBV\SEED`, **în afara OneDrive** | prin GitHub: **Pull** la început, **Commit + Push** la final |
| `SEED_extras` (arhivele de date, copii de siguranță, `RENAMES.md`) | `C:\Users\User\OneDrive\work\UNITBV\2026-2027\SEM I\SEED_extras` | automat, prin OneDrive |
| Sursele datelor (`DateLaborator.zip`, `DateProiecte.zip`) | `C:\Users\User\OneDrive\work\UNITBV\SETURI_DE_DATE` | automat, prin OneDrive |

Nu puneți repository-ul în OneDrive: sincronizarea simultană creează copii de conflict (`…-DESKTOP-XXXX.ipynb`) și poate strica folderul `.git`.

Pe un calculator nou: GitHub Desktop → **File → Clone repository** → `SEED` → în `C:\UNITBV\SEED`. Apoi, dacă lucrați local cu notebook-urile, mediul Python se creează ca în [ghidul local](ghid-local.md).

Pentru că `SEED_extras` nu mai stă lângă repository, scripturile care o folosesc primesc calea **explicit** (vezi secțiunea 2).

## 1. Prima publicare (o singură dată, ~30 minute)

1. Cont GitHub (cu emailul universității poți cere beneficiile gratuite GitHub Education) și **GitHub Desktop** instalat.
2. Numele de utilizator GitHub (`sbildea`) este deja setat în `seed/catalog.py`, iar linkurile Colab și imaginile îl folosesc direct. La un cont nou, înlocuiește-l în tot repository-ul (căutare/înlocuire a lui `sbildea`) și rulează `python tools/genereaza_readme.py`.

3. În GitHub Desktop: **File → Add local repository** → alege folderul `C:\UNITBV\SEED` → „create a repository" (fără README, există deja). Scrie un rezumat, de exemplu `Publicare inițială curs`, apoi **Commit to main** și **Publish repository**.
4. Debifează „Keep this code private". Link-urile **Open in Colab** și descărcarea datelor funcționează doar pentru repository-uri **publice**.
5. Verifică pe github.com că README-ul arată corect.

## 2. Publicarea seturilor de date (release `date-v1`)

Seturile mari de date nu stau în repository; sunt fișiere atașate la un release, de unde le descarcă funcția `incarca`.

1. Arhivele sunt gata în `SEED_extras\release-assets\` din OneDrive (31 de fișiere `.zip`). Nu trebuie reconstruite decât dacă schimbați datele. Pentru reconstruire, din `C:\UNITBV\SEED`, în PowerShell (cele trei căi sunt obligatorii):

   ```powershell
   python tools/construieste_seturi_date.py `
       --seturi    "C:\Users\User\OneDrive\work\UNITBV\SETURI_DE_DATE" `
       --date-curs "C:\Users\User\OneDrive\work\UNITBV\2026-2027\SEM I\ADS1\date.zip" `
       --iesire    "C:\Users\User\OneDrive\work\UNITBV\2026-2027\SEM I\SEED_extras\release-assets"
   ```

   - `--seturi`: folderul cu `DateLaborator.zip` și `DateProiecte.zip`;
   - `--date-curs`: arhiva `date.zip` cu datele de la curs (folderele `csv/`, `xlsx/`, `json/`);
   - `--iesire`: unde se scriu arhivele; arhivele existente cu același nume sunt înlocuite.

   Seturile `proiect-04` și `proiect-16` se descarcă direct de pe Kaggle (este nevoie de internet).

2. Pe github.com: **Releases → Draft a new release** → tag `date-v1`, titlu „Seturi de date".
3. Trage toate fișierele `.zip` în zona de atașamente, apoi **Publish release**.
4. Test: deschide un notebook de temă în Colab, rulează configurarea și `incarca("lab-set1")`.

Pentru a adăuga un set nou: adaugă-l în `seed/catalog.py`, pune arhiva `<nume>.zip` în release-ul `date-v1` (sau creează `date-v2` și schimbă `TAG_DATE`).

Înainte de publicare, poți testa local cu arhivele din folder:

```powershell
$env:SEED_DATE_LOCAL = "C:\Users\User\OneDrive\work\UNITBV\2026-2027\SEM I\SEED_extras\release-assets"
```

(Variabila este valabilă doar în fereastra PowerShell curentă; porniți Jupyter / VS Code din aceeași fereastră.)

## Structura cursului

Șapte module (`cursuri/01-…` … `cursuri/07-…`), câte unul la două săptămâni: 2h curs + 2h seminar. În fiecare modul:

- `curs-*`: materialele de curs (PDF/PPTX și notebook-uri); ultimul notebook de curs se încheie cu **puntea curs → seminar** (concepte, cererea către AI, ce se verifică);
- `seminar-*`: seminarul aplicat, care pornește de la aceeași punte; studenții scriu cererile, verifică și interpretează;
- `tema-*`: temele; `extra-*`: materialele din anii anteriori, cu cod complet, păstrate ca referință;
- `README.md`: pagina modulului (problema de business, materiale în ordine, puntea). Textul punților și al seminariilor poate fi editat direct.

Structura comună a unui modul (problema de business, rolul studentului, conceptele, puntea, seminarul, tema) și lista de verificare pentru un modul nou sunt în [sablon-modul.md](sablon-modul.md).

Notebook-urile de *prompting* din modulul 1 (`curs-01b-prompting-*`) folosesc `bop_utils.py` și cheia API Gemini personală a fiecărui student (Colab Secrets / variabila de mediu `GOOGLE_API_KEY`, la singular). Modelul implicit este `gemini-flash-lite-latest`, cu limite gratuite largi; se poate schimba cu variabila `SEED_GEMINI_MODEL`. Dacă studenții ating limita, `get_completion` afișează un mesaj în română, nu o eroare. Nu puneți chei API în repository; `.gitignore` blochează fișierele de tip `google_api*.txt`.

## 3. Actualizări zilnice

1. Modifici fișierele în folderul `SEED` ca de obicei.
2. În GitHub Desktop: rezumat scurt → **Commit** → **Push origin**.
3. Când modifici un `.pptx`, exportă din nou PDF-ul (PowerPoint: File → Export → PDF).
4. Notebook nou: copiază primele trei celule (antet, badge Colab, „Configurare curs") dintr-un notebook existent din aceeași săptămână și actualizează numele fișierului în badge. Apoi rulează `python tools/genereaza_readme.py`.
5. La teme: șterge rezultatele (Edit → Clear all outputs) înainte de commit.

## 4. Pagina cursului (opțional, GitHub Pages)

Settings → Pages → Source „Deploy from a branch", branch `main`, folder `/ (root)`. După un minut site-ul este la `https://<utilizator>.github.io/SEED/`.

## 5. Lista de verificare anuală (septembrie)

- [ ] Actualizează anul și programul în `README.md` și `docs/prezentare-generala.md`.
- [ ] Exportă din nou PDF-urile slide-urilor modificate.
- [ ] Deschide fiecare notebook din badge-ul Colab, rulează configurarea și toate celulele; repară ce nu merge.
- [ ] Verifică avertismentele de la `pip install` și actualizează `requirements.txt` dacă imaginea Colab s-a schimbat.
- [ ] Commit și push.
- [ ] **Releases → Draft a new release**, tag `2026-2027`, titlu „Anul universitar 2026-2027"; atașează un ZIP cu toate PDF-urile; **Publish release**.
- [ ] Pune link-ul cursului pe platforma de e-learning și verifică-l dintr-o fereastră privată.

## Probleme frecvente

| Problemă | Soluție |
| --- | --- |
| GitHub refuză un fișier | Are peste 100 MB. Pune-l ca arhivă în release-ul de date și adaugă-l în `seed/catalog.py`. |
| „Open in Colab" dă eroare | Repository-ul e privat sau calea / ramura din link e greșită. |
| `incarca` dă eroare 404 | Arhiva lipsește din release-ul `date-v1` sau numele nu coincide cu cel din catalog. |
| `FileNotFoundError` pentru date | Notebook-ul folosește o cale locală; înlocuiește cu `./date/fisier.csv` (relativ la notebook) sau cu `incarca(...)`. |
| Diferențe uriașe între versiuni pe GitHub | S-au salvat rezultatele în notebook. Edit → Clear all outputs înainte de commit. |

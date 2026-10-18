# Modulul 7: Proiect: de la întrebare la decizie

2 ore de curs + 2 ore de seminar. La curs înțelegem conceptele; la seminar le aplicăm lucrând cu un asistent AI.

**Problema de business.** Clientul vostru este setul de date din proiect: *„Ce ne spun datele și ce decizie ar trebui să luăm?”*

- **Rolul vostru:** analist, consultant și consultant de implementare: duceți singuri tot fluxul, de la întrebare la recomandare.
- **Ce predați la final:** notebook-ul proiectului (rulează complet de la zero) și un raport scurt pentru un manager, cu recomandarea, dovezile și limitele analizei.

**Curs**

- [curs-07-de-la-analiza-la-recomandare](curs-07-de-la-analiza-la-recomandare.ipynb) · [Open in Colab](https://colab.research.google.com/github/sbildea/SEED/blob/main/cursuri/07-proiect/curs-07-de-la-analiza-la-recomandare.ipynb)

**Seminar**

- [seminar-07-de-la-intrebare-la-decizie](seminar-07-de-la-intrebare-la-decizie.ipynb) · [Open in Colab](https://colab.research.google.com/github/sbildea/SEED/blob/main/cursuri/07-proiect/seminar-07-de-la-intrebare-la-decizie.ipynb)

**Descrierea proiectelor:** [descriere-proiecte.ipynb](descriere-proiecte.ipynb)

## Puntea curs → seminar

**Concepte cheie**

1. **Fluxul complet:** întrebare → date → explorare → pregătire → model → evaluare → decizie.
2. **Reproductibilitate:** notebook-ul rulează de la început la sfârșit, cu `random_state` fixat.
3. **Comunicarea rezultatelor:** pentru cine nu știe statistică; cifre, nu impresii.
4. **Limitele modelului:** ce nu poate spune și unde poate greși.

**Ce ceri asistentului AI** (exemplu de cerere)

> Pe baza rezultatelor din notebook-ul meu, scrie un rezumat de 5 propoziții pentru un manager: întrebarea, datele, modelul ales, cât de bun este pe datele de test și ce decizie recomand. Menționează o limită a analizei.

**Ce verifici înainte să accepți rezultatul**

- [ ] fiecare cifră din rezumat apare în rezultatele notebook-ului;
- [ ] notebook-ul rulează complet după **Runtime → Restart and run all**;
- [ ] limitele sunt menționate cinstit (date, metrică, generalizare).


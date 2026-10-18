# Modulul 1: Date, întrebări și lucrul cu AI

2 ore de curs + 2 ore de seminar. La curs înțelegem conceptele; la seminar le aplicăm lucrând cu un asistent AI.

**Structura cursului (2h):** 1h concepte despre date și întrebări (slide-urile de mai jos) + 1h curs intensiv de *prompting* (notebook-urile `curs-01b-prompting-1` … `5`, care folosesc Gemini cu o cheie API personală gratuită) și slide-urile despre programarea asistată de AI (de adăugat ca `curs-01c-programare-asistata-ai.pdf`).

**Curs**

- [curs-01-introducere](curs-01-introducere.pdf) (PDF)
- [curs-01b-prompting-1-principii-si-tactici](curs-01b-prompting-1-principii-si-tactici.ipynb) · [Open in Colab](https://colab.research.google.com/github/sbildea/SEED/blob/main/cursuri/01-date-intrebari-ai/curs-01b-prompting-1-principii-si-tactici.ipynb)
- [curs-01b-prompting-2-iterare](curs-01b-prompting-2-iterare.ipynb) · [Open in Colab](https://colab.research.google.com/github/sbildea/SEED/blob/main/cursuri/01-date-intrebari-ai/curs-01b-prompting-2-iterare.ipynb)
- [curs-01b-prompting-3-rezumare](curs-01b-prompting-3-rezumare.ipynb) · [Open in Colab](https://colab.research.google.com/github/sbildea/SEED/blob/main/cursuri/01-date-intrebari-ai/curs-01b-prompting-3-rezumare.ipynb)
- [curs-01b-prompting-4-inferare](curs-01b-prompting-4-inferare.ipynb) · [Open in Colab](https://colab.research.google.com/github/sbildea/SEED/blob/main/cursuri/01-date-intrebari-ai/curs-01b-prompting-4-inferare.ipynb)
- [curs-01b-prompting-5-transformare](curs-01b-prompting-5-transformare.ipynb) · [Open in Colab](https://colab.research.google.com/github/sbildea/SEED/blob/main/cursuri/01-date-intrebari-ai/curs-01b-prompting-5-transformare.ipynb)

**Seminar**

- [seminar-01-primul-notebook-cu-ai](seminar-01-primul-notebook-cu-ai.ipynb) · [Open in Colab](https://colab.research.google.com/github/sbildea/SEED/blob/main/cursuri/01-date-intrebari-ai/seminar-01-primul-notebook-cu-ai.ipynb)

**Temă**

- [tema-01-exercitii-python](tema-01-exercitii-python.ipynb) · [Open in Colab](https://colab.research.google.com/github/sbildea/SEED/blob/main/cursuri/01-date-intrebari-ai/tema-01-exercitii-python.ipynb)

**Extra (referință)** — materiale din anii anteriori, cu cod complet, pentru cine vrea să aprofundeze

- [extra-01-instructiuni-anaconda](extra-01-instructiuni-anaconda.pdf) (PDF)
- [extra-01-recapitulare-python](extra-01-recapitulare-python.ipynb) · [Open in Colab](https://colab.research.google.com/github/sbildea/SEED/blob/main/cursuri/01-date-intrebari-ai/extra-01-recapitulare-python.ipynb)

## Puntea curs → seminar

**Concepte cheie**

1. O analiză de date pornește de la o **întrebare** la care datele pot răspunde.
2. **Tipuri de date:** numerice, categoriale, ordinale, dată/timp; fiecare cere alte metode.
3. **Observație** (rând) și **variabilă** (coloană); **ținta** (ce vrem să prezicem) și **predictorii**.
4. Asistentul AI scrie codul; **tu** formulezi întrebarea și **verifici** rezultatul.
5. **Prompting:** o cerere bună are context, sarcină clară, constrângeri și formatul răspunsului; exemplele și pașii expliciți îmbunătățesc rezultatul.

**Ce ceri asistentului AI** (exemplu de cerere)

> Încarcă setul `lab-set1` cu `incarca("lab-set1")[0]` și descrie tabelul: câte rânduri și coloane are, ce tip de date are fiecare coloană și care coloană pare să fie variabila țintă. Explică pe scurt fiecare pas.

**Ce verifici înainte să accepți rezultatul**

- [ ] dimensiunile afișate sunt cele reale (`df.shape`);
- [ ] tipurile au sens: o coloană numerică citită ca text (de exemplu `TotalCharges`) este un semnal de date murdare;
- [ ] asistentul nu a inventat coloane care nu există în `df.columns`.


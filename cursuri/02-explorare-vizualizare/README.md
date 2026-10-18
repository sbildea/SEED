# Modulul 2: Analiza exploratorie și vizualizarea datelor

2 ore de curs + 2 ore de seminar. La curs înțelegem conceptele; la seminar le aplicăm lucrând cu un asistent AI.

**Curs**

- [curs-02-analiza-exploratorie](curs-02-analiza-exploratorie.pdf) (PDF)
- [curs-02-vizualizarea-datelor](curs-02-vizualizarea-datelor.ipynb) · [Open in Colab](https://colab.research.google.com/github/prof/SEED/blob/main/cursuri/02-explorare-vizualizare/curs-02-vizualizarea-datelor.ipynb)
- [curs-02-vizualizarea-datelor](curs-02-vizualizarea-datelor.pdf) (PDF)

**Seminar**

- [seminar-02-explorare-vizualizare](seminar-02-explorare-vizualizare.ipynb) · [Open in Colab](https://colab.research.google.com/github/prof/SEED/blob/main/cursuri/02-explorare-vizualizare/seminar-02-explorare-vizualizare.ipynb)

**Temă**

- [tema-02a-dataframe-analiza-exploratorie](tema-02a-dataframe-analiza-exploratorie.ipynb) · [Open in Colab](https://colab.research.google.com/github/prof/SEED/blob/main/cursuri/02-explorare-vizualizare/tema-02a-dataframe-analiza-exploratorie.ipynb)
- [tema-02b-vizualizarea-datelor](tema-02b-vizualizarea-datelor.ipynb) · [Open in Colab](https://colab.research.google.com/github/prof/SEED/blob/main/cursuri/02-explorare-vizualizare/tema-02b-vizualizarea-datelor.ipynb)

**Extra (referință)** — materiale din anii anteriori, cu cod complet, pentru cine vrea să aprofundeze

- [extra-02-dataframe](extra-02-dataframe.ipynb) · [Open in Colab](https://colab.research.google.com/github/prof/SEED/blob/main/cursuri/02-explorare-vizualizare/extra-02-dataframe.ipynb)
- [extra-02-vizualizarea-datelor](extra-02-vizualizarea-datelor.ipynb) · [Open in Colab](https://colab.research.google.com/github/prof/SEED/blob/main/cursuri/02-explorare-vizualizare/extra-02-vizualizarea-datelor.ipynb)

## Puntea curs → seminar

**Concepte cheie**

1. **Distribuții:** centru (medie, mediană), împrăștiere (abatere standard, IQR), asimetrie.
2. **Valori lipsă și valori aberante:** cum le detectăm și ce decidem să facem cu ele.
3. **Relații între variabile:** corelație, tabele încrucișate; corelația nu înseamnă cauzalitate.
4. **Graficul potrivit întrebării:** histogramă, boxplot, scatter, bar chart, heatmap.

**Ce ceri asistentului AI** (exemplu de cerere)

> Pentru tabelul `OnlineRetail` din `lab-set4`, arată distribuția coloanei `Quantity` cu o histogramă și un boxplot, identifică valorile negative și explică ce reprezintă. Apoi elimină-le și refă graficele.

**Ce verifici înainte să accepți rezultatul**

- [ ] graficele au titlu și axe cu sens; scala nu ascunde datele (valori extreme);
- [ ] știi câte rânduri au fost eliminate și de ce;
- [ ] graficul răspunde la întrebarea pusă, nu la una asemănătoare.


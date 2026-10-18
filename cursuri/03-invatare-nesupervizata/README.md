# Modulul 3: Învățare nesupervizată: PCA, clusterizare, asociere

2 ore de curs + 2 ore de seminar. La curs înțelegem conceptele; la seminar le aplicăm lucrând cu un asistent AI.

**Curs**

- [curs-03a-pca-clusterizare](curs-03a-pca-clusterizare.ipynb) · [Open in Colab](https://colab.research.google.com/github/prof/SEED/blob/main/cursuri/03-invatare-nesupervizata/curs-03a-pca-clusterizare.ipynb)
- [curs-03b-asociere-recomandari](curs-03b-asociere-recomandari.ipynb) · [Open in Colab](https://colab.research.google.com/github/prof/SEED/blob/main/cursuri/03-invatare-nesupervizata/curs-03b-asociere-recomandari.ipynb)

**Seminar**

- [seminar-03-invatare-nesupervizata](seminar-03-invatare-nesupervizata.ipynb) · [Open in Colab](https://colab.research.google.com/github/prof/SEED/blob/main/cursuri/03-invatare-nesupervizata/seminar-03-invatare-nesupervizata.ipynb)

**Temă**

- [tema-03-invatare-nesupervizata](tema-03-invatare-nesupervizata.ipynb) · [Open in Colab](https://colab.research.google.com/github/prof/SEED/blob/main/cursuri/03-invatare-nesupervizata/tema-03-invatare-nesupervizata.ipynb)

**Extra (referință)** — materiale din anii anteriori, cu cod complet, pentru cine vrea să aprofundeze

- [extra-03-asociere-recomandari](extra-03-asociere-recomandari.ipynb) · [Open in Colab](https://colab.research.google.com/github/prof/SEED/blob/main/cursuri/03-invatare-nesupervizata/extra-03-asociere-recomandari.ipynb)
- [extra-03-pca-clusterizare](extra-03-pca-clusterizare.ipynb) · [Open in Colab](https://colab.research.google.com/github/prof/SEED/blob/main/cursuri/03-invatare-nesupervizata/extra-03-pca-clusterizare.ipynb)

## Puntea curs → seminar

**Concepte cheie**

1. **Distanța** între observații și de ce **scalarea** contează.
2. **PCA:** comprimăm multe coloane în câteva componente, păstrând cât mai multă varianță.
3. **k-means:** grupuri de observații asemănătoare; alegerea lui K (metoda cotului, silhouette).
4. **Reguli de asociere:** suport, încredere, lift (ce produse se cumpără împreună).

**Ce ceri asistentului AI** (exemplu de cerere)

> Pentru tabelul `general_data` din `lab-set2`, standardizează coloanele numerice (fără coloana țintă `Attrition` și fără ID-uri), aplică PCA și arată cât din varianță explică primele componente. Apoi aplică k-means pentru K de la 2 la 8 și afișează scorul silhouette pentru fiecare K.

**Ce verifici înainte să accepți rezultatul**

- [ ] datele au fost scalate înainte de PCA și k-means;
- [ ] ținta și coloanele de tip ID au fost excluse;
- [ ] grupurile sunt interpretate prin mediile coloanelor originale, nu doar prin numărul grupului.


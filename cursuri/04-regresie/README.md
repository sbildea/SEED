# Modulul 4: Regresie: modele liniare, supraînvățare, regularizare

2 ore de curs + 2 ore de seminar. La curs înțelegem conceptele; la seminar le aplicăm lucrând cu un asistent AI.

**Curs**

- [curs-04-bias-variance](curs-04-bias-variance.pdf) (PDF)
- [curs-04-regresie](curs-04-regresie.pdf) (PDF)
- [curs-04-regresori-liniari](curs-04-regresori-liniari.pdf) (PDF)
- [curs-04-regularizare-lasso-ridge](curs-04-regularizare-lasso-ridge.pdf) (PDF)
- [curs-04-regularizare](curs-04-regularizare.pdf) (PDF)
- [curs-04a-regresie-uni-multivariata](curs-04a-regresie-uni-multivariata.ipynb) · [Open in Colab](https://colab.research.google.com/github/prof/SEED/blob/main/cursuri/04-regresie/curs-04a-regresie-uni-multivariata.ipynb)
- [curs-04b-regularizarea-regresiei](curs-04b-regularizarea-regresiei.ipynb) · [Open in Colab](https://colab.research.google.com/github/prof/SEED/blob/main/cursuri/04-regresie/curs-04b-regularizarea-regresiei.ipynb)

**Seminar**

- [seminar-04-regresie](seminar-04-regresie.ipynb) · [Open in Colab](https://colab.research.google.com/github/prof/SEED/blob/main/cursuri/04-regresie/seminar-04-regresie.ipynb)

**Extra (referință)** — materiale din anii anteriori, cu cod complet, pentru cine vrea să aprofundeze

- [extra-04-exercitii-regresie-boston](extra-04-exercitii-regresie-boston.ipynb) · [Open in Colab](https://colab.research.google.com/github/prof/SEED/blob/main/cursuri/04-regresie/extra-04-exercitii-regresie-boston.ipynb)
- [extra-04-regresori-ml](extra-04-regresori-ml.ipynb) · [Open in Colab](https://colab.research.google.com/github/prof/SEED/blob/main/cursuri/04-regresie/extra-04-regresori-ml.ipynb)

## Puntea curs → seminar

**Concepte cheie**

1. **Modelul liniar** și interpretarea coeficienților.
2. **Măsuri de eroare:** R², MAE, RMSE, MAPE; ce spune fiecare.
3. **Supraînvățare** și compromisul **bias-variance**: train bun, test slab.
4. **Regularizare:** Ridge și Lasso penalizează coeficienții mari; Lasso poate elimina predictori.

**Ce ceri asistentului AI** (exemplu de cerere)

> Pe tabelul `train` din `lab-set6`, prezice `SalePrice` cu regresie liniară folosind 5 predictori numerici aleși după corelația cu ținta. Pune deoparte 20% date de test, raportează RMSE și R² pe antrenare și pe test, apoi compară cu Ridge și Lasso cu `alpha` ales prin validare încrucișată.

**Ce verifici înainte să accepți rezultatul**

- [ ] setul de test a fost separat înainte de alegerea predictorilor și a lui `alpha`;
- [ ] compari eroarea pe antrenare cu cea pe test (supraînvățare?);
- [ ] semnul și mărimea coeficienților au sens pentru problemă.


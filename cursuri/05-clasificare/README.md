# Modulul 5: Clasificare: regresie logistică, arbori, ansambluri, SVM

2 ore de curs + 2 ore de seminar. La curs înțelegem conceptele; la seminar le aplicăm lucrând cu un asistent AI.

**Problema de business.** Operatorul de telecomunicații: *„Care clienți urmează să plece?”*

- **Rolul vostru:** analist de date: comparați mai multe modele de clasificare și explicați ce fel de greșeli face fiecare.
- **Ce predați la final:** comparația a cel puțin trei modele pe `lab-set1`, cu matricea de confuzie și o recomandare argumentată pentru unul dintre ele.

**Curs**

- [curs-05a-regresie-logistica](curs-05a-regresie-logistica.ipynb) · [Open in Colab](https://colab.research.google.com/github/sbildea/SEED/blob/main/cursuri/05-clasificare/curs-05a-regresie-logistica.ipynb)
- [curs-05b-clasificare](curs-05b-clasificare.ipynb) · [Open in Colab](https://colab.research.google.com/github/sbildea/SEED/blob/main/cursuri/05-clasificare/curs-05b-clasificare.ipynb)
- [curs-05c-svm](curs-05c-svm.ipynb) · [Open in Colab](https://colab.research.google.com/github/sbildea/SEED/blob/main/cursuri/05-clasificare/curs-05c-svm.ipynb)
- [curs-05c-svm](curs-05c-svm.pdf) (PDF)

**Seminar**

- [seminar-05-clasificare](seminar-05-clasificare.ipynb) · [Open in Colab](https://colab.research.google.com/github/sbildea/SEED/blob/main/cursuri/05-clasificare/seminar-05-clasificare.ipynb)

**Temă**

- [tema-05-clasificatori](tema-05-clasificatori.ipynb) · [Open in Colab](https://colab.research.google.com/github/sbildea/SEED/blob/main/cursuri/05-clasificare/tema-05-clasificatori.ipynb)

**Extra (referință)** — materiale din anii anteriori, cu cod complet, pentru cine vrea să aprofundeze

- [extra-05-balansarea-claselor](extra-05-balansarea-claselor.pdf) (PDF): Balansarea claselor (slide-uri)
- [extra-05-exercitii-regresie-logistica](extra-05-exercitii-regresie-logistica.ipynb) · [Open in Colab](https://colab.research.google.com/github/sbildea/SEED/blob/main/cursuri/05-clasificare/extra-05-exercitii-regresie-logistica.ipynb)
- [extra-05-tuning-clasic](extra-05-tuning-clasic.ipynb) · [Open in Colab](https://colab.research.google.com/github/sbildea/SEED/blob/main/cursuri/05-clasificare/extra-05-tuning-clasic.ipynb)

## Puntea curs → seminar

**Concepte cheie**

1. **Probabilitate și prag de decizie:** regresia logistică dă o probabilitate; pragul o transformă în clasă.
2. **Frontiera de decizie:** liniară (logistică, SVM liniar) sau flexibilă (arbori, kNN, SVM cu kernel).
3. **Arbori și ansambluri:** un arbore e ușor de explicat; random forest și boosting sunt mai precise.
4. **Matricea de confuzie:** fals pozitivi și fals negativi au costuri diferite.

**Ce ceri asistentului AI** (exemplu de cerere)

> Pe `lab-set1`, prezice `Churn` cu regresie logistică și cu random forest. Pune deoparte 20% date de test stratificat, codifică variabilele categoriale într-un pipeline, apoi afișează matricea de confuzie și raportul de clasificare pentru fiecare model. Explică ce înseamnă un fals negativ pentru firmă.

**Ce verifici înainte să accepți rezultatul**

- [ ] împărțirea train/test este stratificată, iar codificarea este învățată doar pe antrenare;
- [ ] uită-te la recall și precision pe clasa minoritară, nu doar la acuratețe;
- [ ] poți explica de ce un model e mai bun decât celălalt pentru *această* problemă.


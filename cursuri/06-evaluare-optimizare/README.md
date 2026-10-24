# Modulul 6: Evaluare și optimizare: metrici, validare încrucișată, Optuna

2 ore de curs + 2 ore de seminar. La curs înțelegem conceptele; la seminar le aplicăm lucrând cu un asistent AI.

**Problema de business.** Managerul de retenție: *„Fiecare ofertă ne costă bani. Câți clienți să contactăm, cât câștigăm și de unde știu că va funcționa și luna viitoare?”*

- **Rolul vostru:** consultant: alegeți metrica din costurile clientului, evaluați corect și transformați rezultatul în bani.
- **Ce predați la final:** pragul de decizie recomandat și profitul estimat pe date noi, cu ipotezele folosite, într-un rezumat pentru manager.

**Curs**

- [curs-06-evaluare-optimizare](curs-06-evaluare-optimizare.ipynb) · [Open in Colab](https://colab.research.google.com/github/sbildea/SEED/blob/main/cursuri/06-evaluare-optimizare/curs-06-evaluare-optimizare.ipynb)

**Seminar**

- [seminar-06-validare-incrucisata-optuna](seminar-06-validare-incrucisata-optuna.ipynb) · [Open in Colab](https://colab.research.google.com/github/sbildea/SEED/blob/main/cursuri/06-evaluare-optimizare/seminar-06-validare-incrucisata-optuna.ipynb)

**Extra (referință)** — materiale din anii anteriori, cu cod complet, pentru cine vrea să aprofundeze

- [extra-06-pipeline-uri](extra-06-pipeline-uri.pdf) (PDF): Linii de procesare / pipeline (slide-uri)
- [extra-06-exemplu-clasificator-svm](extra-06-exemplu-clasificator-svm.ipynb) · [Open in Colab](https://colab.research.google.com/github/sbildea/SEED/blob/main/cursuri/06-evaluare-optimizare/extra-06-exemplu-clasificator-svm.ipynb)
- [extra-06-optuna-dashboard-script](extra-06-optuna-dashboard-script.ipynb) · [Open in Colab](https://colab.research.google.com/github/sbildea/SEED/blob/main/cursuri/06-evaluare-optimizare/extra-06-optuna-dashboard-script.ipynb)
- [extra-06-optuna-dashboard](extra-06-optuna-dashboard.ipynb) · [Open in Colab](https://colab.research.google.com/github/sbildea/SEED/blob/main/cursuri/06-evaluare-optimizare/extra-06-optuna-dashboard.ipynb)
- [extra-06-optuna-studiu-logreg](extra-06-optuna-studiu-logreg.ipynb) · [Open in Colab](https://colab.research.google.com/github/sbildea/SEED/blob/main/cursuri/06-evaluare-optimizare/extra-06-optuna-studiu-logreg.ipynb)
- [extra-06-optuna-studiu-xgboost](extra-06-optuna-studiu-xgboost.ipynb) · [Open in Colab](https://colab.research.google.com/github/sbildea/SEED/blob/main/cursuri/06-evaluare-optimizare/extra-06-optuna-studiu-xgboost.ipynb)

## Puntea curs → seminar

**Concepte cheie**

1. **Metrica vine din problemă:** recall, precision, F1, ROC-AUC sau RMSE, după costul greșelilor.
2. **Validarea încrucișată:** o estimare stabilă, în locul unei singure împărțiri norocoase.
3. **Data leakage:** setul de test se folosește o singură dată; transformările stau în pipeline.
4. **Optimizare cu buget:** Optuna caută hiperparametrii mai eficient decât grid search.

**Ce ceri asistentului AI** (exemplu de cerere)

> Folosind Optuna cu validare încrucișată stratificată în 5 ture, optimizează recall pentru prezicerea `AHD` din `Heart.csv`, comparând regresia logistică și random forest, cu buget de 60 de secunde și `random_state=17`. Pune deoparte 20% date de test înainte și evaluează pe ele o singură dată, cu matrice de confuzie.

**Ce verifici înainte să accepți rezultatul**

- [ ] setul de test a fost separat înainte de Optuna și nu apare în funcția obiectiv;
- [ ] transformările sunt în pipeline sau învățate doar pe antrenare;
- [ ] metrica optimizată este cea argumentată din problemă;
- [ ] poți explica diferența dintre scorul CV și scorul de test.


# Modulul 5: Clasificare: regresie logistică, arbori, ansambluri, SVM

2 ore de curs + 2 ore de seminar. La curs înțelegem conceptele; la seminar le aplicăm lucrând cu un asistent AI.

**Problema de business.** Operatorul de telecomunicații: *„Care clienți urmează să plece?”*

- **Rolul vostru:** analist de date: comparați mai multe modele de clasificare și explicați ce fel de greșeli face fiecare.
- **Ce predați la final:** comparația a cel puțin trei modele pe `lab-set1` și pe setul proiectului, cu modelul de referință, matricea de confuzie a modelului ales și o recomandare argumentată.

**Legătura cu proiectul.** Proiectul este un clasificator pe setul vostru de date, cu **cel puțin trei modele comparate**. La curs înțelegem cum decide fiecare model; la seminar rulăm **arena** (același protocol pentru toate modelele) pe `lab-set1` și pe datele proiectului.

**Curs**

- [curs-05a-regresie-logistica](curs-05a-regresie-logistica.ipynb) · [Open in Colab](https://colab.research.google.com/github/sbildea/SEED/blob/main/cursuri/05-clasificare/curs-05a-regresie-logistica.ipynb): capitolele 0-4: cererea vagă, acuratețea care minte, de la dreaptă la probabilitate, matricea de confuzie, pragul și curba ROC
- [curs-05b-clasificare](curs-05b-clasificare.ipynb) · [Open in Colab](https://colab.research.google.com/github/sbildea/SEED/blob/main/cursuri/05-clasificare/curs-05b-clasificare.ipynb): capitolele 5-9: kNN, arborele de decizie, random forest și gradient boosting, SVM, arena

**Seminar**

- [seminar-05-clasificare](seminar-05-clasificare.ipynb) · [Open in Colab](https://colab.research.google.com/github/sbildea/SEED/blob/main/cursuri/05-clasificare/seminar-05-clasificare.ipynb): arena pe `lab-set1` și pe setul proiectului

**Temă**

- [tema-05-clasificatori](tema-05-clasificatori.ipynb) · [Open in Colab](https://colab.research.google.com/github/sbildea/SEED/blob/main/cursuri/05-clasificare/tema-05-clasificatori.ipynb): depistarea diabetului (datele Pima, `./date/`)

**Extra (referință)** — materiale din anii anteriori, cu cod complet, pentru cine vrea să aprofundeze

- [extra-05-logistica-heart](extra-05-logistica-heart.ipynb) · [Open in Colab](https://colab.research.google.com/github/sbildea/SEED/blob/main/cursuri/05-clasificare/extra-05-logistica-heart.ipynb): regresia logistică pe `Heart.csv`: sigmoida animată, logit, interacțiuni, `C`
- [extra-05-knn-arbori-pima](extra-05-knn-arbori-pima.ipynb) · [Open in Colab](https://colab.research.google.com/github/sbildea/SEED/blob/main/cursuri/05-clasificare/extra-05-knn-arbori-pima.ipynb): kNN, arbori și random forest pe datele Pima
- [extra-05-svm](extra-05-svm.ipynb) · [Open in Colab](https://colab.research.google.com/github/sbildea/SEED/blob/main/cursuri/05-clasificare/extra-05-svm.ipynb): SVM: vectori suport, `C`, kernel, SVR
- [extra-05-svm](extra-05-svm.pdf) (PDF): SVM (slide-uri)
- [extra-05-tuning-clasic](extra-05-tuning-clasic.ipynb) · [Open in Colab](https://colab.research.google.com/github/sbildea/SEED/blob/main/cursuri/05-clasificare/extra-05-tuning-clasic.ipynb): căutarea hiperparametrilor cu `GridSearchCV` (introducere în modulul 6)
- [extra-05-exercitii-regresie-logistica](extra-05-exercitii-regresie-logistica.ipynb) · [Open in Colab](https://colab.research.google.com/github/sbildea/SEED/blob/main/cursuri/05-clasificare/extra-05-exercitii-regresie-logistica.ipynb): exerciții de regresie logistică

## Puntea curs → seminar

**Concepte cheie** (modulul 5)

1. **Probabilitate și prag:** clasificatorul dă o probabilitate; pragul o transformă în clasă, iar 0,5 nu e o lege.
2. **Referința și împărțirea stratificată:** acuratețea se citește față de clasa majoritară.
3. **Matricea de confuzie:** fals pozitivi și fals negativi au costuri diferite; recall, precizie; AUC compară modele fără prag.
4. **Cum decid modelele:** regresia logistică (sigmoidă), kNN (vecini; cere scalare), arborele (reguli; memorează fără limită de adâncime), random forest și gradient boosting (mulți arbori), SVM (marginea cea mai largă; cere scalare).
5. **Arena:** același protocol (împărțire, `Pipeline`, referință, metrici) pentru toate modelele, într-un singur tabel; supraînvățarea se vede ca diferență mare între antrenare și test.

**Ce ceri asistentului AI** (exemplu de cerere)

> Pe `lab-set1`, fără `customerID`, cu `TotalCharges` transformat în număr (golurile = 0), împarte 80/20 stratificat (`random_state=42`). Într-un `Pipeline` cu completarea lipsurilor, one-hot și (unde trebuie) standardizare, compară clasa majoritară, regresia logistică, un arbore cu `max_depth=5` și random forest. Pentru fiecare: acuratețea pe antrenare și pe test, recall, precizie și AUC pe test, într-un singur tabel; apoi matricea de confuzie pentru modelul cel mai bun.

**Ce verifici înainte să accepți rezultatul**

- [ ] ID-urile sunt scoase, iar coloanele „numerice” stocate ca text au fost convertite;
- [ ] împărțirea este stratificată, iar pregătirea e în `Pipeline`, învățată doar pe antrenare;
- [ ] tabelul are un rând „clasa majoritară”;
- [ ] te uiți la recall, precizie și AUC, nu doar la acuratețe;
- [ ] compari antrenarea cu testul (un arbore nelimitat?);
- [ ] poți explica, pentru modelul ales, cum decide și ce greșeli face.

# Modulul 4: Regresie: modele liniare, supraînvățare, regularizare

2 ore de curs + 2 ore de seminar. La curs înțelegem conceptele; la seminar le aplicăm lucrând cu un asistent AI.

**Problema de business.** O agenție imobiliară: *„Cât să cerem pe o casă și cât de mult poate greși estimarea?”*

- **Rolul vostru:** analist de date: construiți un model de estimare și spuneți cât de mult poate greși.
- **Ce predați la final:** estimarea prețului pentru locuințele din `lab-set6`, cu eroarea medie exprimată în dolari, un interval de eroare și principalii factori care influențează prețul.

**Legătura cu proiectul.** Proiectul vostru este un clasificator (modulul 5), dar protocolul învățat aici se folosește neschimbat: împărțirea train/test, modelul de referință, pregătirea în `Pipeline`, supraînvățarea și regularizarea.

**Curs**

- [curs-04a-regresie-uni-multivariata](curs-04a-regresie-uni-multivariata.ipynb) · [Open in Colab](https://colab.research.google.com/github/sbildea/SEED/blob/main/cursuri/04-regresie/curs-04a-regresie-uni-multivariata.ipynb): capitolele 0-4: cererea vagă, împărțirea și modelul de referință, o dreaptă, mai mulți predictori, supraînvățarea
- [curs-04b-regularizarea-regresiei](curs-04b-regularizarea-regresiei.ipynb) · [Open in Colab](https://colab.research.google.com/github/sbildea/SEED/blob/main/cursuri/04-regresie/curs-04b-regularizarea-regresiei.ipynb): capitolele 5-8: o singură împărțire minte, Ridge, Lasso, Elastic Net și clasamentul, ce îi spunem clientului

Slide-uri opționale (teorie): [bias-variance](curs-04-bias-variance.pdf), [regresie](curs-04-regresie.pdf), [regresori liniari](curs-04-regresori-liniari.pdf), [regularizare](curs-04-regularizare.pdf), [Lasso și Ridge](curs-04-regularizare-lasso-ridge.pdf).

**Seminar**

- [seminar-04-regresie](seminar-04-regresie.ipynb) · [Open in Colab](https://colab.research.google.com/github/sbildea/SEED/blob/main/cursuri/04-regresie/seminar-04-regresie.ipynb)

**Temă**

- [tema-04-regresie](tema-04-regresie.ipynb) · [Open in Colab](https://colab.research.google.com/github/sbildea/SEED/blob/main/cursuri/04-regresie/tema-04-regresie.ipynb): prețul mașinilor second-hand (`date-curs`, tabelul `audi`)

**Extra (referință)** — materiale din anii anteriori, cu cod complet, pentru cine vrea să aprofundeze

- [extra-04-regresie-clasica](extra-04-regresie-clasica.ipynb) · [Open in Colab](https://colab.research.google.com/github/sbildea/SEED/blob/main/cursuri/04-regresie/extra-04-regresie-clasica.ipynb): statsmodels, p-values, variabile categoriale, valori aberante, selecție pas cu pas
- [extra-04-lasso-ridge-detalii](extra-04-lasso-ridge-detalii.ipynb) · [Open in Colab](https://colab.research.google.com/github/sbildea/SEED/blob/main/cursuri/04-regresie/extra-04-lasso-ridge-detalii.ipynb): Lasso și Ridge pe King County: efectul scalării asupra coeficienților, Elastic Net
- [extra-04-regresori-ml](extra-04-regresori-ml.ipynb) · [Open in Colab](https://colab.research.google.com/github/sbildea/SEED/blob/main/cursuri/04-regresie/extra-04-regresori-ml.ipynb): kNN, arbori, random forest, boosting pentru regresie (după modulul 5)
- [extra-04-exercitii-regresie-boston](extra-04-exercitii-regresie-boston.ipynb) · [Open in Colab](https://colab.research.google.com/github/sbildea/SEED/blob/main/cursuri/04-regresie/extra-04-exercitii-regresie-boston.ipynb): exerciții din anii anteriori (setul Boston, scos din scikit-learn din motive etice; de folosit doar ca exemplu)

## Puntea curs → seminar

**Concepte cheie** (modulul 4)

1. **Ținta și împărțirea:** train/test o singură dată, la început; evaluăm doar pe test (nu pe un tabel fără țintă și nu pe antrenare).
2. **Modelul de referință** (media) și măsurile **MAE, RMSE** (în unitățile țintei) și **R²**.
3. **Coeficienții:** efectul unui predictor când ceilalți rămân la fel; depind de ce alte coloane sunt în model.
4. **Supraînvățarea:** bun pe antrenare, slab pe test; apare ușor cu multe coloane și puține rânduri. O singură împărțire poate fi norocoasă sau ghinionistă.
5. **Pipeline:** completarea lipsurilor, one-hot și scalarea se învață doar pe antrenare.
6. **Regularizarea:** Ridge strânge coeficienții, Lasso îi poate anula, Elastic Net le combină; `alpha` se alege prin validare încrucișată.

**Ce ceri asistentului AI** (exemplu de cerere)

> Pe tabelul `train` din `lab-set6`, fără `Id`, împarte 80/20 (`random_state=42`). Într-un `Pipeline` cu completarea lipsurilor, one-hot și standardizare, compară media (model de referință), regresia liniară, `RidgeCV`, `LassoCV` și `ElasticNetCV`. Raportează într-un singur tabel MAE și R² pe antrenare și pe test și spune câți coeficienți a anulat Lasso.

**Ce verifici înainte să accepți rezultatul**

- [ ] `Id` și ținta nu sunt printre predictori; evaluarea e pe partea de test din `train`, nu pe tabelul `test` fără preț;
- [ ] tabelul are un rând „model de referință”;
- [ ] pregătirea (lipsuri, one-hot, scalare) e în `Pipeline`, învățată doar pe antrenare;
- [ ] compari antrenarea cu testul (supraînvățare?);
- [ ] `alpha` a fost ales prin validare încrucișată, nu după scorul pe test;
- [ ] coeficienții au semn și mărime plauzibile pentru problemă.

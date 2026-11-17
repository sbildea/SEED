# Cosmetizarea modulelor 4 și 5 (propunere finală, de discutat)

Document de lucru, 2026-11-17. Nu s-a modificat niciun notebook. Pornește de la propunerea anterioară (scrisă în conversație, doar pentru modulul 4), o verifică pe date și o extinde la modulul 5.

Toate cifrele marcate cu ✔ au fost calculate pe 2026-11-17 cu `.venv` (scikit-learn 1.9), cu `random_state=42` și 80/20 train/test, pe o pregătire minimă: coloanele numerice cu valorile lipsă puse pe 0 sau `get_dummies` pe tot tabelul. Când se scriu notebook-urile, valorile de control se **recalculează** pe pregătirea exactă din notebook.

---

## 1. Auditul propunerii anterioare

### 1.1 Ce rămâne valabil

| Afirmație | Verdict |
|---|---|
| Modulul 4 e scris în formatul vechi: `04a` + `04b` au 192 de celule (95 de cod), 63 de celule cu ieșiri salvate, 4 seturi de date diferite în curs și un al cincilea (`lab-set6`) în seminar | ✔ corect |
| Detaliile (statsmodels, p-values, `stepwise`, GAM, validare încrucișată scrisă de mână) încarcă inutil cursul și trebuie mutate în extra-uri | ✔ corect |
| Puntea curs → seminar e copiată de 3 ori; nu există `tema-04`; celula „TEMA 5” din `04b` folosește Boston | ✔ corect. Boston a fost scos din scikit-learn în versiunea 1.2 din motive etice (coloana `B`), deci nu e un set potrivit pentru temă |
| Un singur fir roșu: agenția imobiliară pe `lab-set6/train` | ✔ bun, e deja în README și în seminar |
| Tabelul `test` din `lab-set6` nu are `SalePrice` (capcană: agentul încearcă să evalueze pe el) | ✔ verificat |
| Câteva case uriașe vândute ieftin trag dreapta | ✔ sunt 4 case peste 4.000 sqft. Doar 2 sunt ieftine (Id 524: 184.750 $; Id 1299: 160.000 $); celelalte 2 costă peste 745.000 $ |
| Teza „protocolul e conceptul, modelul e o linie” | ✔ ideea centrală bună, păstrată |

### 1.2 Ce e greșit sau neconfirmat

| Afirmație | Ce arată datele | Corecție |
|---|---|---|
| Capitolul 0 „modelul prea bun”: regresia pe toate coloanele dă R² ≈ 0,9x pe antrenare și e slabă pe test | ✘ Pe toate coloanele numerice, R² e **0,809 pe antrenare și 0,830 pe test**: nu există supraînvățare. Cu one-hot (287 de coloane): 0,937 / 0,887. | Supraînvățarea se arată cu **puține case și multe coloane**: 150 de case × 287 de coloane dau ✔ **R² = 1,00 pe antrenare și 0,34 pe test**. E un rezultat spectaculos și adevărat. |
| `Id` ca predictor e o capcană vizibilă | ✘ coeficientul lui `Id` e −2,18 $, efect neglijabil | `Id` rămâne regulă în primer, nu capcană de scenă |
| `GarageCars` și `GarageArea` își schimbă semnul (multicoliniaritate) | ✘ Nu se reproduce. Corelația dintre ele e 0,882 ✔, dar ambii coeficienți rămân pozitivi. | Multicoliniaritatea se arată prin **coeficientul care se micșorează**: `GarageCars` scade de la 66.911 $ (singur) la 11.202 $ (cu alți 5 predictori) ✔. Mesajul: „coeficientul depinde de ce altceva e în model” |
| „dolari pe metru pătrat” | ✘ Ames e în **picioare pătrate** | 102,5 $ pe sqft ✔ (≈ 1.100 $/m², de spus explicit) |
| Modelul-bază are „R² = 0 din definiție” | pe test e −0,001 ✔ | corect ca idee; în text: „≈ 0, poate fi și negativ pe test” |
| Arena din capitolul 6 cu kNN, arbori, random forest, boosting | ✘ **ordine greșită:** kNN, arborii și ansamblurile se predau în **modulul 5** | Arena se mută în modulul 5 (vezi 2.2), unde comparația a cel puțin 3 modele e chiar livrabilul. În modulul 4 rămâne o singură „cutie neagră” ca teaser. |
| Capcana „un model câștigă la un `random_state` și pierde la altul” | ✘ Random forest câștigă la toate cele 5 împărțiri testate | Faptul real e mai util: **aceeași regresie dă R² pe test între 0,51 și 0,85 doar schimbând `random_state`** ✔ (0: 0,64; 1: 0,82; 2: 0,85; 3: 0,51; 4: 0,84). O singură împărțire poate minți. |
| „Printre seturile din catalog nu văd altul potrivit pentru tema 4” | ✘ ratat: `date-curs` are 5 tabele de **mașini second-hand** (`audi`: 10.668 × 9: `model, year, price, transmission, mileage, fuelType, tax, mpg, engineSize`) ✔ | Set ideal pentru temă: țintă numerică (`price`), categorii puține, alt domeniu decât Ames |
| Timpi de 15-20 min pe capitol | prea dens față de ritmul modulului 3 (8-12 min/capitol) | 6-7 capitole scurte; restul trece în seminar și extra |

### 1.3 Ce a lipsit cu totul

1. **Modulul 5 nu a fost analizat.** Are aceleași probleme, mai accentuate (secțiunea 3).
2. **Suprapunerea cu modulul 6.** `curs-06` predă deja generalizarea, modelul de referință, arborele care memorează, pipeline-ul, validarea încrucișată, căutarea hiperparametrilor și scorul „prea bun” ca semnal de alarmă. Propunerea anterioară le preda pe toate în modulul 4. Trebuie o **împărțire clară a conceptelor pe module** (secțiunea 2.1).
3. **Modulele 6 și 7 nu mai există pe disc.** Commitul `f766a66` le-a scos din git („rămân local”), dar folderele de aici conțin doar `date/` și `test.sqlite3`. Ele se recuperează din istoric (`git show f766a66^:cursuri/06-evaluare-optimizare/...`). **De verificat** dacă există pe celălalt calculator, înainte de orice lucru pe ele.
4. **One-hot e deja predat** în modulul 3 (Referință R1b și tema 3). Modulul 4 îl folosește și trimite la R1b, nu îl repredă.
5. **Distanța și scalarea sunt deja predate** în capitolul 1 din `curs-03a`. kNN-ul din modulul 5 trimite acolo.

---

## 2. Principiul comun pentru modulele 4, 5 și 6

### 2.1 Un singur protocol, introdus treptat

Studentul învață **o rețetă care nu depinde de model**: date curate → împărțire → model de referință → `Pipeline(pregătire, model)` → metrică pe test → interpretare. Modelul e o linie care se schimbă.

| Concept | Modulul 4 (regresie) | Modulul 5 (clasificare) | Modulul 6 (evaluare) |
|---|---|---|---|
| Train/test, „nu evaluăm pe antrenare” | **introdus** | folosit (stratificat) | folosit |
| Modelul de referință | **introdus** (media) | folosit (clasa majoritară) | folosit |
| Supraînvățarea | **introdusă** (150 de case) | revăzută (arborele) | aprofundată |
| Instabilitatea unei singure împărțiri | **arătată** (R² 0,51-0,85) | – | **validarea încrucișată predată** |
| `alpha` ales prin validare încrucișată | folosit ca „cutie” (`RidgeCV`) | – | explicat |
| Pipeline (scalare fără scurgere) | **introdus** la regularizare | folosit | aprofundat |
| Metrica în bani | eroarea în dolari | costul FN vs. FP, **numit** | **calculat** (profit, prag) |
| Arena de modele | teaser (un random forest) | **arena completă** | căutarea hiperparametrilor |

### 2.2 Recuzita comună: `evalueaza(model)`

O celulă vizibilă (nu ascunsă într-un pachet), copiată identic în `04b`, `05` și seminarii:

```python
def evalueaza(model, X_train, X_test, y_train, y_test, nume):
    model.fit(X_train, y_train)
    # regresie: MAE, RMSE, R² pe antrenare și pe test; clasificare: acuratețe, recall, AUC
    ...
    return rand_pentru_clasament
```

- Agentului i se cere **doar modelul nou**, nu toată evaluarea. Asta elimină scurgerile și comparațiile inegale, iar mesajul „alt model = o linie” se vede în cod.
- Fiecare apel adaugă un rând într-un **clasament**. Modelul de referință e mereu primul rând.

---

## 3. Modulul 4: plan final

**Problema:** agenția imobiliară: *„Cât să cerem pe o casă și cât de mult poate greși estimarea?”* Toată ora pe `lab-set6/train`.

### 3.1 `curs-04a-regresie` (≈ 55 min)

| # | Capitol | Live | Capcană | Control ✔ |
|---|---|---|---|---|
| 0 | **Cererea vagă** | „prezice prețul caselor din `lab-set6`” | agentul ia tabelul `test`, fără `SalePrice`, sau evaluează pe antrenare | `test` are 80 de coloane, `train` 81 |
| 1 | **Ghicitul mediei** | modelul-bază: fiecare casă = media | un R² fără bază nu spune nimic | MAE bază ≈ **62.576 $**, R² ≈ 0 |
| 2 | **O dreaptă** | `GrLivArea` → `SalePrice`, coeficient, reziduuri | casele 524 și 1299 (uriașe și ieftine) | **102,5 $/sqft**, R² test 0,554, MAE 38.341 $ |
| 3 | **Mai mulți predictori** | 6 predictori, „toate celelalte egale”; categoriile cu one-hot (trimitere la R1b din modulul 3) | coeficientul depinde de vecinii lui; `MSSubClass` e numeric dar categorial; „NA” la `PoolQC` înseamnă „fără piscină” | `GarageCars` 66.911 $ → 11.202 $; toate numericele: R² test 0,83, MAE 22.232 $ |
| 4 | **Prea multe coloane, prea puține case** | 150 de case × 287 de coloane | R² perfect pe antrenare | **1,00 / 0,34** |

### 3.2 `curs-04b-regularizare` (≈ 50 min)

| # | Capitol | Live | Capcană | Control ✔ |
|---|---|---|---|---|
| 5 | **O singură împărțire minte** | aceeași regresie la 5 valori `random_state` | „modelul meu are R² 0,85” | R² test între **0,51 și 0,85** |
| 6 | **Regularizarea** | Ridge pe aceleași 150 de case; Lasso pe tot setul; `Pipeline(StandardScaler, …)`; graficul traseelor coeficienților | scalarea făcută înainte de împărțire | Ridge pe 150 de case: **0,34 → 0,85**; Lasso: R² 0,888, **234 din 288 de coeficienți = 0** |
| 7 | **O cutie neagră** (teaser) | `evalueaza(RandomForestRegressor())`: o linie | „mai precis” nu înseamnă „explicabil”; detalii în modulul 5 | RF: R² 0,888, MAE 18.232 $ |
| 8 | **Ce îi spunem clientului** | eroarea în dolari plus un interval din cuantilele reziduurilor | o cifră exactă e o promisiune falsă | se calculează în notebook |

Urmează Referința (RSS, MAE/RMSE/MAPE/R², Ridge/Lasso în LaTeX, logaritmul ținței: asimetria lui `SalePrice` e 1,88 ✔), apoi puntea unică și Jurnalul de sesiune.

### 3.3 Extra-uri pentru modulul 4 (trimitere într-un rând: „Aprofundare: …” la finalul capitolului)

| Extra | Conținut | Sursă | Capitol |
|---|---|---|---|
| `extra-04-statistica-regresiei` | statsmodels, p-values, AIC, `stepwise`, influență (Cook) | apendicele `04a` și King County | 3 |
| ~~`extra-04-validare-de-la-zero`~~ | **renunțat (decizia 4):** PRESS scris de mână nu se mai folosește; celulele au fost scoase | – | – |
| `extra-04-lasso-ridge-in-detaliu` | standard vs. min-max, Elastic Net, graficele Plotly | `04b` | 6 |
| `extra-04-categorii-si-transformari` | categorii cu multe niveluri (cod poștal), ordonate, logaritm, polinoame | `04a`, celulele 92-102 | 3, Referință |
| `extra-04-regresori-ml` (există) | kNN, arbori, RF, XGBoost cu `GridSearchCV` | – | 7 (de citit după modulul 5) |
| `extra-04-exercitii-regresie-boston` | se arhivează sau se trece pe `date-curs` | – | – |

`LungDisease`, `CarPrice`, `house_sales` rămân în `./date/` doar pentru extra-uri. PDF-urile (bias-variance, regularizare) se leagă din Referință.

### 3.4 Seminar și temă

- **Seminar:** pe `lab-set6`, păstrat, dar cu exercițiile aliniate la capitole (bază → dreaptă → multivariată → Ridge/Lasso cu `evalueaza`), apoi setul proiectului.
- **`tema-04` (nouă):** `date-curs`, tabelul `audi` sau alt brand, cu `random_state` în enunț. Cerințe: bază, regresie, Lasso, interval de eroare în lire, Jurnal. Fără rezolvare.

---

## 4. Modulul 5: plan final

### 4.1 Diagnostic

| | Stare | Problemă |
|---|---|---|
| `05a` | 100 de celule (51 de cod), 44 cu ieșiri | ținta din README (Telco) nu apare; cursul folosește `Heart.csv` |
| `05b` | 81 de celule, 26k caractere de text, 15 cu ieșiri | Pima de două ori (kNN, arbori); celula „Administrative: cerințe proiect docx” e veche; „Data viitoare: SVM” |
| `05c` | 54 de celule (36 de cod), 4,7k caractere de text | demonstrație de cod fără explicații; un exemplu de **regresie** (SVR pe `petrol_consumption`) într-un modul de clasificare |
| Toate | – | imagini ca `attachment:image.png` (nu se văd în Colab după copiere); puntea copiată de 3 ori; 4 seturi (Heart, Pima, sintetice, petrol) |
| Seminar și temă | pe `lab-set1` și Pima | OK, dar nu reiau capitolele cursului |

### 4.2 Firul roșu: `lab-set1` (Telco), același client ca în modulul 6

Valori verificate ✔: 7.043 × 21; `TotalCharges` e **text**, cu 11 valori goale; 26,5% plecări. Modelul „nimeni nu pleacă” are acuratețe **0,734**. Regresia logistică dă 0,804, dar prinde doar **57,5%** din cei care pleacă. Un arbore nelimitat are 0,999 pe antrenare și **0,719 pe test, sub modelul care nu face nimic**.

### 4.3 `curs-05a-logistica-si-prag` (≈ 55 min)

| # | Capitol | Capcană | Control ✔ |
|---|---|---|---|
| 0 | **Cererea vagă:** „prezice cine pleacă” | `TotalCharges` ca text; `customerID` | 11 goluri |
| 1 | **Acuratețea care minte** | 73,4% fără niciun model | 0,734 |
| 2 | **De la dreaptă la probabilitate:** sigmoida, logistica pe 1 predictor (`tenure`) | regresia liniară dă „probabilități” sub 0 | se calculează |
| 3 | **Pragul și matricea de confuzie:** FN vs. FP, recall, precizie | pragul 0,5 nu e o lege; costul în bani vine în modulul 6 | acuratețe 0,804, recall 0,575 |

### 4.4 `curs-05b-arena` (≈ 55 min)

| # | Capitol | Capcană | Control ✔ |
|---|---|---|---|
| 4 | **Vecinii (kNN):** trimitere la distanța din `curs-03a` | fără scalare decid `TotalCharges` și `MonthlyCharges` | se calculează |
| 5 | **Arborele:** reguli citibile | arborele nelimitat memorează | **0,999 / 0,719** |
| 6 | **Arena:** `evalueaza(model)` pentru logistică, kNN, arbore limitat, RF, gradient boosting; fiecare grup aduce un model | câștigătorul la acuratețe ≠ câștigătorul la recall | se calculează |
| 7 | **Ce îi spunem clientului:** ce model, ce greșeli face, pe cine ratează | – | – |

ROC/AUC intră în Referință și se folosește în modulul 6. SVM devine extra.

### 4.5 Extra-uri pentru modulul 5

| Extra | Sursă |
|---|---|
| `extra-05-logistica-pe-heart` (coeficienți, cote, interacțiuni, regularizare `C`, animația sigmoidei) | `05a` |
| `extra-05-arbori-si-knn-pe-pima` (criterii Gini/entropie, desenarea arborelui, parametri) | `05b` |
| `extra-05-svm` (actualul `05c` + pdf/pptx; SVR primește trimitere și din modulul 4) | `05c` |
| `extra-05-tuning-clasic` (există) | – |
| `extra-05-exercitii-regresie-logistica` (există) | – |

**Tema 5** rămâne pe Pima, care e alt set decât cursul. Capcana firească pentru temă: zerourile din `glucose`, `bp`, `bmi` sunt de fapt valori lipsă (de verificat).

---

## 5. Reguli transversale (ca în modulul 3)

- Formatul pe capitole: Concept → Prezice → Cere agentului → Verifică → Capcană → Pentru client.
- Primer per modul. Reguli pentru 4-5: scoate `Id`/`customerID`; împarte înainte de orice transformare; mereu un model de referință; scalare în `Pipeline`; `random_state` din enunț; nu evalua pe `test` fără țintă.
- Referință la final; puntea **o singură dată** (ultimul notebook de curs, seminar, README); Jurnal de sesiune.
- Zero ieșiri salvate; fiecare notebook rulează de la zero în mai puțin de un minut (RF cu `n_estimators=100`); imagini din `raw.githubusercontent.com` sau LaTeX, fără atașamente.
- Fișierele `.pptx` nu se modifică de agent.

---

## 6. Decizii pentru tine

1. **Arena în modulul 5** (curs) sau în seminarul 5?
2. **Tema 4 pe `date-curs` (mașini)**: de acord? Ce brand?
3. **Modulele 6-7 lipsesc de pe acest disc**: există pe celălalt calculator, sau le recuperez din `f766a66^`?
4. **Ordinea de lucru propusă:** `curs-04a` → verificat de tine în sală → `04b` → seminar/temă 4 → extra 4 → modulul 5 cu același tipar.

---

## 7. Decizii și stare (2026-11-17, ciclul 2)

### Deciziile tale

| # | Decizie |
|---|---|
| 0 | Modulele 6 și 7 există pe celălalt calculator; nu le recuperăm din istoric. |
| 1 | Modulele 4-5 se restrâng la conceptele necesare proiectului (un clasificator pe setul fiecărui student, cel puțin 3 modele). **Arena:** modelele se explică *conceptual* la curs (`curs-05b`), antrenarea practică se face la seminar (`seminar-05`). |
| 2 | Tema 4 pe `date-curs`, tabelul `audi`. |
| 3 | (= 0) |
| 4 | Fără PRESS / validare încrucișată scrisă de mână; Ridge, Lasso și Elastic Net sunt suficiente. Restul se aplică ambelor module. |

### Ce s-a făcut (necomis)

**Modulul 4**
- `curs-04a-regresie-uni-multivariata` (rescris, 24 de celule, ~4 s): capitolele 0-4, Referință R1-R5, Jurnal.
- `curs-04b-regularizarea-regresiei` (rescris, 25 de celule, ~5 s): capitolele 5-8 (Ridge, Lasso, Elastic Net), „Ce îi spunem clientului”, Referință, puntea unică.
- `seminar-04-regresie` (aliniat la capitole; „pe proiect” = pregătirea setului pentru clasificare) și **`tema-04-regresie` (nouă, `audi`)**.
- Extra-uri: vechiul `curs-04a` → `extra-04-regresie-clasica` (fără celulele PRESS); vechiul `curs-04b` → `extra-04-lasso-ridge-detalii` (fără „TEMA 5”).

**Modulul 5**
- `curs-05a-regresie-logistica` (rescris, 28 de celule, ~3 s): Telco, capitolele 0-4 (cererea vagă, acuratețea care minte, sigmoida, matricea de confuzie, pragul și ROC).
- `curs-05b-clasificare` (rescris, 28 de celule, ~10 s): kNN, arbore, random forest și gradient boosting, SVM, arena; harta frontierei de decizie pentru fiecare model.
- `seminar-05-clasificare` (arena pe `lab-set1`, apoi pe proiect) și `tema-05-clasificatori` (Pima, ținta corectată în `Outcome`, fără Optuna/grid search).
- Extra-uri: vechiul `curs-05a` → `extra-05-logistica-heart`, vechiul `curs-05b` → `extra-05-knn-arbori-pima`, `curs-05c-svm` (.ipynb, .pdf, .pptx) → `extra-05-svm`.

**Comune:** celula „Configurare curs” nouă în toate notebook-urile modulelor 4-5; primer per modul; README-urile modulelor și tabelul din README-ul principal regenerate (`tools/genereaza_readme.py`). Recuzita `pregatire()` și `evalueaza()` este identică în 04b, 05a și 05b.

### Valori de control noi, găsite la execuție
- `sample_submission` din `lab-set6` **are** o coloană `SalePrice`, cu prețuri de exemplu: capcană în capitolul 0.
- Singura casă cu `RoofMatl = ClyTile` este casa 1299 (cea atipică): Lasso o pune pe locul 2 la importanță. Capcana „categorii rare” din capitolul 7.
- `ElasticNetCV` cu lista implicită de `alpha` alege chiar capătul listei (R² 0,57); cu lista 0,01-10.000, R² 0,87. Capcana „alpha la marginea listei”.
- În arena Telco **câștigă regresia logistică** (AUC 0,842), înaintea gradient boosting (0,833) și random forest (0,820).
- kNN fără scalare are acuratețe *mai mare* (0,790 față de 0,776), dar recall mult mai mic (0,385 față de 0,567).
- La tema 4 (`audi`), regularizarea nu aduce câștig (multe rânduri, puține coloane): întrebare de interpretare în exercițiul 3.

### Rămâne de făcut / de verificat
- [ ] Citit de tine: textul capitolelor, mai ales formulările pentru client.
- [ ] Rulare în Colab (local: toate notebook-urile de curs, seminar, temă și extra-urile modificate rulează fără erori, cu `.venv`).
- [ ] Modulul 6 (pe celălalt calculator): trimiteri la `curs-05c-svm` sau la vechile `curs-05a/b` trebuie actualizate; recuzita `evalueaza` poate fi refolosită acolo.
- [ ] `extra-04-regresori-ml` și `extra-04-exercitii-regresie-boston` folosesc încă setul Boston (doar actualizată celula de configurare).
- [ ] Commit, după revizuire.

# Seturile de date ale cursului

Toate seturile se încarcă la fel, în Colab sau local:

```python
from seed.date import incarca, lista_seturi
lista_seturi()                 # lista de mai jos
date = incarca("lab-set2")     # toate tabelele: date["general_data"] sau date[1]
df = incarca("lab-set2", "general_data")   # direct un singur tabel
```

Pentru lucrul fără internet, descarcă-le dinainte: `python tools/descarca_seturi.py` (vezi [ghidul local](ghid-local.md)).

## Date folosite la curs

| Nume | Descriere | Tabele (poziție: nume, rânduri × coloane) | Sursa |
|---|---|---|---|
| `date-curs` | Date demonstrative curs: mașini second-hand (CSV), COVID ICU (XLSX), recenzii vinuri (JSON) | [0] `audi`: 10.668 × 9<br>[1] `bmw`: 10.781 × 9<br>[2] `cclass`: 3.899 × 7<br>[3] `focus`: 5.454 × 7<br>[4] `ford`: 17.965 × 9<br>[5] `hyundi`: 4.860 × 9<br>[6] `merc`: 13.119 × 9<br>[7] `skoda`: 6.267 × 9<br>[8] `toyota`: 6.738 × 9<br>[9] `unclean cclass`: 4.006 × 11<br>[10] `unclean focus`: 5.604 × 11<br>[11] `vauxhall`: 13.632 × 9<br>[12] `vw`: 15.157 × 9<br>[13] `winemag-data-130k-v2`: 129.971 × 13<br>[14] `Kaggle_Sirio_Libanes_ICU_Prediction`: 1.925 × 231 | [link](https://www.kaggle.com/datasets/adityadesai13/used-car-dataset-ford-and-mercedes) |

## Seturi de laborator

| Nume | Descriere | Tabele (poziție: nume, rânduri × coloane) | Sursa |
|---|---|---|---|
| `lab-set1` | Telco Customer Churn - clienți care renunță la abonament | [0] `WA_Fn-UseC_-Telco-Customer-Churn`: 7.043 × 21 | [link](https://www.kaggle.com/blastchar/telco-customer-churn) |
| `lab-set2` | HR Analytics - plecarea angajaților (5 tabele, cheie EmployeeID) | [0] `employee_survey_data`: 4.410 × 4<br>[1] `general_data`: 4.410 × 24<br>[2] `in_time`: 4.410 × 262<br>[3] `manager_survey_data`: 4.410 × 3<br>[4] `out_time`: 4.410 × 262 | [link](https://www.kaggle.com/vjchoudhary7/hr-analytics-case-study) |
| `lab-set3` | Consumul de alcool și performanța școlară (matematică, portugheză) | [0] `student-mat`: 395 × 33<br>[1] `student-por`: 649 × 33 | [link](https://www.kaggle.com/uciml/student-alcohol-consumption) |
| `lab-set4` | Online Retail - tranzacții magazin online (UCI) | [0] `OnlineRetail`: 541.909 × 8 | [link](https://www.kaggle.com/jihyeseo/online-retail-data-set-from-uci-ml-repo) |
| `lab-set5` | Bank Loan Status - acordarea creditelor | [0] `credit_test`: 10.353 × 18<br>[1] `credit_train`: 100.514 × 19 | [link](https://www.kaggle.com/zaurbegiev/my-dataset) |
| `lab-set6` | House Prices - prețuri locuințe (Ames, Iowa) | [0] `test`: 1.459 × 80<br>[1] `train`: 1.460 × 81<br>[2] `sample_submission`: 1.459 × 2 | [link](https://www.kaggle.com/c/house-prices-advanced-regression-techniques) |
| `lab-set7` | Healthcare Provider Fraud - fraude la furnizori medicali (8 tabele) | [0] `Test_Beneficiarydata-1542969243754`: 63.968 × 25<br>[1] `Test_Inpatientdata-1542969243754`: 9.551 × 30<br>[2] `Test_Outpatientdata-1542969243754`: 125.841 × 27<br>[3] `Test-1542969243754`: 1.353 × 1<br>[4] `Train_Beneficiarydata-1542865627584`: 138.556 × 25<br>[5] `Train_Inpatientdata-1542865627584`: 40.474 × 30<br>[6] `Train_Outpatientdata-1542865627584`: 517.737 × 27<br>[7] `Train-1542865627584`: 5.410 × 2 | [link](https://www.kaggle.com/rohitrox/healthcare-provider-fraud-detection-analysis) |
| `lab-set8` | European Soccer Database - meciuri și jucători (SQLite, 7 tabele) | [0] `Country`: 11 × 2<br>[1] `League`: 11 × 3<br>[2] `Match`: 25.979 × 115<br>[3] `Player`: 11.060 × 7<br>[4] `Player_Attributes`: 183.978 × 42<br>[5] `Team`: 299 × 5<br>[6] `Team_Attributes`: 1.458 × 25 | [link](https://www.kaggle.com/hugomathien/soccer) |
| `lab-set9` | Healthcare - predicția accidentului vascular cerebral | [0] `test_2v`: 18.601 × 11<br>[1] `train_2v`: 43.400 × 12 | [link](https://www.kaggle.com/asaumya/healthcare-problem-prediction-stroke-patients) |
| `lab-set10` | Medical Appointment No-Shows - neprezentarea la programări | [0] `KaggleV2-May-2016`: 110.527 × 14 | [link](https://www.kaggle.com/joniarroba/noshowappointments) |

## Seturi pentru proiecte

| Nume | Descriere | Tabele (poziție: nume, rânduri × coloane) | Sursa |
|---|---|---|---|
| `proiect-01` | Credit score classification | [0] `train`: 100.000 × 28 | [link](https://www.kaggle.com/datasets/parisrohan/credit-score-classification) |
| `proiect-02` | Top Spotify songs 2023 | [0] `spotify-2023`: 953 × 24 | [link](https://www.kaggle.com/datasets/nelgiriyewithana/top-spotify-songs-2023) |
| `proiect-03` | Employee dataset | [0] `Employee`: 4.653 × 9 | [link](https://www.kaggle.com/datasets/tawfikelmetwally/employee-dataset) |
| `proiect-04` | Abandon curs online (LMS) | [0] `xAPI-Edu-Data`: 480 × 17 | [link](https://www.kaggle.com/datasets/aljarah/xAPI-Edu-Data) |
| `proiect-05` | Water quality and potability | [0] `water_potability`: 3.276 × 10 | [link](https://www.kaggle.com/datasets/uom190346a/water-quality-and-potability) |
| `proiect-06` | Smoking and drinking (Coreea) | [0] `smoking_driking_dataset_Ver01`: 991.346 × 24 | [link](https://www.kaggle.com/datasets/sooyoungher/smoking-drinking-dataset) |
| `proiect-07` | Weather in Australia - RainTomorrow | [0] `weatherAUS`: 145.460 × 23 | [link](https://www.kaggle.com/datasets/jsphyg/weather-dataset-rattle-package) |
| `proiect-08` | Diabetes health indicators | [0] `diabetes_binary_5050split_health_indicators_BRFSS2015`: 70.692 × 22 | [link](https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset) |
| `proiect-09` | COVID-19 patients | [0] `Covid Data`: 1.048.575 × 21 | [link](https://www.kaggle.com/datasets/meirnizri/covid19-dataset) |
| `proiect-10` | Pharyngitis (streptococ) | [0] `pharyngitis`: 676 × 20 | [link](https://www.kaggle.com/datasets/yoshifumimiya/pharyngitis) |
| `proiect-11` | GoalZone fitness classes | [0] `fitness_class_2212`: 1.500 × 8 | [link](https://www.kaggle.com/datasets/ddosad/datacamps-data-science-associate-certification) |
| `proiect-12` | Telco customer churn | [0] `WA_Fn-UseC_-Telco-Customer-Churn`: 7.043 × 21 | [link](https://www.kaggle.com/blastchar/telco-customer-churn) |
| `proiect-13` | HR analytics | [0] `data_dictionary`: 52 × 4<br>[1] `employee_survey_data`: 4.410 × 4<br>[2] `general_data`: 4.410 × 24<br>[3] `manager_survey_data`: 4.410 × 3 | [link](https://www.kaggle.com/vjchoudhary7/hr-analytics-case-study) |
| `proiect-14` | Stroke prediction | [0] `healthcare-dataset-stroke-data`: 5.110 × 12 | [link](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset) |
| `proiect-15` | Medical appointment no-shows | [0] `KaggleV2-May-2016`: 110.527 × 14 | [link](https://www.kaggle.com/joniarroba/noshowappointments) |
| `proiect-16` | Spanish wine quality | [0] `wines_SPA`: 7.500 × 11 | [link](https://www.kaggle.com/datasets/fedesoriano/spanish-wine-quality-dataset) |
| `proiect-17` | Lead score case study | [0] `Leads`: 9.240 × 37 | [link](https://www.kaggle.com/datasets/amolbhone/lead-score-case-study) |
| `proiect-18` | Kickstarter projects | [0] `kickstarter_projects`: 374.853 × 11 | [link](https://www.kaggle.com/datasets/ulrikthygepedersen/kickstarter-projects) |
| `proiect-19` | Car fuel type | [0] `fueltype`: 1.498.740 × 8 | [link](https://www.kaggle.com/datasets/fernandin83/carfueltype) |
| `proiect-20` | NBA rookies - logistic regression | [0] `nba_logreg`: 1.340 × 21 | [link](https://data.world/exercises/logistic-regression-exercise-1) |

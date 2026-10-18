"""Catalogul seturilor de date ale cursului SEED.

Fiecare set este o arhivă ZIP publicată ca fișier atașat (asset) la release-ul
`TAG_DATE` din repository-ul GitHub al cursului. `fisiere` dă ordinea tabelelor,
astfel încât `incarca("lab-set5")[1]` să fie mereu același tabel.
"""

GITHUB_USER = "sbildea"
REPO = "SEED"
TAG_DATE = "date-v1"

CATALOG = {
    # --- Date folosite la curs (săptămânile 2-3) ---
    "date-curs": {
        "titlu": "Date demonstrative curs: mașini second-hand (CSV), COVID ICU (XLSX), recenzii vinuri (JSON)",
        "sursa": "https://www.kaggle.com/datasets/adityadesai13/used-car-dataset-ford-and-mercedes",
        "fisiere": [],
    },
    # --- Seturi de laborator ---
    "lab-set1": {
        "titlu": "Telco Customer Churn - clienți care renunță la abonament",
        "sursa": "https://www.kaggle.com/blastchar/telco-customer-churn",
        "fisiere": ["WA_Fn-UseC_-Telco-Customer-Churn.csv"],
    },
    "lab-set2": {
        "titlu": "HR Analytics - plecarea angajaților (5 tabele, cheie EmployeeID)",
        "sursa": "https://www.kaggle.com/vjchoudhary7/hr-analytics-case-study",
        "fisiere": ["employee_survey_data.csv", "general_data.csv", "in_time.csv",
                    "manager_survey_data.csv", "out_time.csv"],
    },
    "lab-set3": {
        "titlu": "Consumul de alcool și performanța școlară (matematică, portugheză)",
        "sursa": "https://www.kaggle.com/uciml/student-alcohol-consumption",
        "fisiere": ["student-mat.csv", "student-por.csv"],
    },
    "lab-set4": {
        "titlu": "Online Retail - tranzacții magazin online (UCI)",
        "sursa": "https://www.kaggle.com/jihyeseo/online-retail-data-set-from-uci-ml-repo",
        "fisiere": ["OnlineRetail.xlsx"],
    },
    "lab-set5": {
        "titlu": "Bank Loan Status - acordarea creditelor",
        "sursa": "https://www.kaggle.com/zaurbegiev/my-dataset",
        "fisiere": ["credit_test.csv", "credit_train.csv"],
    },
    "lab-set6": {
        "titlu": "House Prices - prețuri locuințe (Ames, Iowa)",
        "sursa": "https://www.kaggle.com/c/house-prices-advanced-regression-techniques",
        "fisiere": ["test.csv", "train.csv", "sample_submission.csv"],
    },
    "lab-set7": {
        "titlu": "Healthcare Provider Fraud - fraude la furnizori medicali (8 tabele)",
        "sursa": "https://www.kaggle.com/rohitrox/healthcare-provider-fraud-detection-analysis",
        "fisiere": ["Test_Beneficiarydata-1542969243754.csv",
                    "Test_Inpatientdata-1542969243754.csv",
                    "Test_Outpatientdata-1542969243754.csv",
                    "Test-1542969243754.csv",
                    "Train_Beneficiarydata-1542865627584.csv",
                    "Train_Inpatientdata-1542865627584.csv",
                    "Train_Outpatientdata-1542865627584.csv",
                    "Train-1542865627584.csv"],
    },
    "lab-set8": {
        "titlu": "European Soccer Database - meciuri și jucători (SQLite, 7 tabele)",
        "sursa": "https://www.kaggle.com/hugomathien/soccer",
        "fisiere": ["database.sqlite"],
    },
    "lab-set9": {
        "titlu": "Healthcare - predicția accidentului vascular cerebral",
        "sursa": "https://www.kaggle.com/asaumya/healthcare-problem-prediction-stroke-patients",
        "fisiere": ["test_2v.csv", "train_2v.csv"],
    },
    "lab-set10": {
        "titlu": "Medical Appointment No-Shows - neprezentarea la programări",
        "sursa": "https://www.kaggle.com/joniarroba/noshowappointments",
        "fisiere": ["KaggleV2-May-2016.csv"],
    },
    # --- Seturi pentru proiecte (vezi cursuri/07-proiect/descriere-proiecte.ipynb) ---
    "proiect-01": {"titlu": "Credit score classification", "sursa": "https://www.kaggle.com/datasets/parisrohan/credit-score-classification"},
    "proiect-02": {"titlu": "Top Spotify songs 2023", "sursa": "https://www.kaggle.com/datasets/nelgiriyewithana/top-spotify-songs-2023"},
    "proiect-03": {"titlu": "Employee dataset", "sursa": "https://www.kaggle.com/datasets/tawfikelmetwally/employee-dataset"},
    "proiect-04": {"titlu": "Abandon curs online (LMS)", "sursa": "https://www.kaggle.com/datasets/aljarah/xAPI-Edu-Data"},
    "proiect-05": {"titlu": "Water quality and potability", "sursa": "https://www.kaggle.com/datasets/uom190346a/water-quality-and-potability"},
    "proiect-06": {"titlu": "Smoking and drinking (Coreea)", "sursa": "https://www.kaggle.com/datasets/sooyoungher/smoking-drinking-dataset"},
    "proiect-07": {"titlu": "Weather in Australia - RainTomorrow", "sursa": "https://www.kaggle.com/datasets/jsphyg/weather-dataset-rattle-package"},
    "proiect-08": {"titlu": "Diabetes health indicators", "sursa": "https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset"},
    "proiect-09": {"titlu": "COVID-19 patients", "sursa": "https://www.kaggle.com/datasets/meirnizri/covid19-dataset"},
    "proiect-10": {"titlu": "Pharyngitis (streptococ)", "sursa": "https://www.kaggle.com/datasets/yoshifumimiya/pharyngitis"},
    "proiect-11": {"titlu": "GoalZone fitness classes", "sursa": "https://www.kaggle.com/datasets/ddosad/datacamps-data-science-associate-certification"},
    "proiect-12": {"titlu": "Telco customer churn", "sursa": "https://www.kaggle.com/blastchar/telco-customer-churn"},
    "proiect-13": {"titlu": "HR analytics", "sursa": "https://www.kaggle.com/vjchoudhary7/hr-analytics-case-study"},
    "proiect-14": {"titlu": "Stroke prediction", "sursa": "https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset"},
    "proiect-15": {"titlu": "Medical appointment no-shows", "sursa": "https://www.kaggle.com/joniarroba/noshowappointments"},
    "proiect-16": {"titlu": "Spanish wine quality", "sursa": "https://www.kaggle.com/datasets/fedesoriano/spanish-wine-quality-dataset"},
    "proiect-17": {"titlu": "Lead score case study", "sursa": "https://www.kaggle.com/datasets/amolbhone/lead-score-case-study"},
    "proiect-18": {"titlu": "Kickstarter projects", "sursa": "https://www.kaggle.com/datasets/ulrikthygepedersen/kickstarter-projects"},
    "proiect-19": {"titlu": "Car fuel type", "sursa": "https://www.kaggle.com/datasets/fernandin83/carfueltype"},
    "proiect-20": {"titlu": "NBA rookies - logistic regression", "sursa": "https://data.world/exercises/logistic-regression-exercise-1"},
}

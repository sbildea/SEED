# <img style="float: left; padding-right: 10px; width: 100px" src="../imagini/unitbv_mie.png"> <center>Știința Explorării și Exploatării Datelor - SEED1</center>

## <center>Prezentare generală</center>

**Universitatea Transilvania**<br>
**SIIPA, Semestrul I**<br>
**Instructor:** Conf. dr. Teodor &Scedil;tefan B&icirc;ldea<br>
**Contact:** teodor.bildea@unitbv.ro<br>

### Introducere

&emsp;Acest curs este o introducere în moduri de exploatare a datelor cu ajutorul inteligenței artificiale. Contextul general este cel al datelor pe care un analist de business le va întălni cel mai probabil lucrând cu sisteme ERP, și anume date tabelare. 

Data Science - știința (explorării și exploatării) datelor a devenit o materie de studiu în toate programele care au curiculă informatică. Diversele aspecte ale acestei științe rezonează diferit cu diferite audiențe. În contextul actual se adeverește tot mai mult sintagma „datele sunt noul petrol”.

&emsp;Problemele pe care le vom aborda din perspectiva soluțiilor date de modele de învățare automată sunt cele de clasificare și regresie. Acestea presupun date istorice cu observații ce conțin măsurători numerice asupra datelor ce trebuie estimate prin modelare (date țintă, variabila dependentă)  împreună cu caracteristici/atribute/variabile explicative/variabile independente/covariate ce ajută modelul în asocierea unui context relativ la datele țintă. Un exemplu de <b>învățare cu supervizare</b> ar fi prognoza temperaturii care se bazează pe istoric cu atribute cum ar fi cele legate de vânt, umiditate, perioadă a anului etc.  

&emsp;<b>Învățarea fără supervizare</b> presupune o sarcină de optimizare fără a cunoaște a priori soluții ale problemei. Un exemplu ar fi o clasificare a unui nor de puncte folosind K medii - `K-means clustering`. În acest caz parametrul K trebuie testat, nu se cunoaște numărul de clase căutat.

&emsp;Cursul se adresează viitorilor analiști de date, consultanți, consultanți de implementare și specialiști în știința datelor aplicată. Accentul cade pe **concepte** și pe **rezolvarea de probleme**: la curs înțelegem metodele și când se folosesc, iar la seminar le aplicăm pe date reale, formulând cerințele în limbaj natural pentru un asistent AI care scrie codul. Nu este nevoie să știți să programați în Python; este nevoie să știți ce cereți, să verificați ce primiți și să explicați rezultatul cuiva care nu știe statistică.

&emsp;Cursul are **7 module**, câte unul la două săptămâni: **2 ore de curs + 2 ore de seminar**. Fiecare modul pornește de la o problemă de business (un client cu o întrebare), iar seminarul continuă direct cursul, prin „puntea curs → seminar”: conceptele cheie, cererea către asistentul AI și ce trebuie verificat.

| Modul | Tema | Problema de business |
|---|---|---|
| 1 | Date, întrebări și lucrul cu AI (inclusiv bazele formulării cererilor, *prompting*) | Ce putem afla din datele despre clienți? |
| 2 | Analiza exploratorie și vizualizarea datelor | Ce se vinde, cui și când? Putem avea încredere în cifre? |
| 3 | Învățare nesupervizată: PCA, clusterizare, reguli de asociere | Ce tipuri de clienți / angajați avem? Ce produse se cumpără împreună? |
| 4 | Regresie: modele liniare, supraînvățare, regularizare | Cât valorează o locuință și ce îi crește prețul? |
| 5 | Clasificare: regresie logistică, arbori, ansambluri, SVM | Care clienți urmează să plece? |
| 6 | Evaluare și optimizare: metrici, validare încrucișată, Optuna | Câți clienți contactăm și cât câștigăm? |
| 7 | Proiect: de la analiză la recomandare | Ce decizie recomandăm clientului nostru? |

Materialele fiecărui modul sunt în folderul [`cursuri`](../cursuri) al repository-ului.

## Administrative

- Veți avea la dispoziție seturi de date pentru explorarea ideilor prezentate. 

Lista cu seturile de date disponibile este în [seturi-de-date.md](seturi-de-date.md). Vă voi anunța pe email despre alocarea aleatorie a seturilor de date. Fiecare dintre voi va analiza date pe o temă de clasificare (și potențial una de regresie).
Seturile de date vor fi individuale și vor defini proiectele cu care vă veți prezenta la examenul parțial și la examenul final. Nu trebuie descărcate manual: în notebook, `incarca("proiect-07")` (cu numărul proiectului vostru) aduce datele direct.

- Lucrul practic se face cu ajutorul unui asistent AI: voi formulați cerințele pe baza conceptelor din curs, asistentul scrie codul, voi verificați și interpretați rezultatele. Vezi [ghidul de programare asistată de AI](ghid-programare-asistata-ai.md). Notebook-urile se pot rula în [Google Colab](ghid-colab.md) sau [local, pe calculatorul vostru](ghid-local.md).

- După seminarii va exista o temă aplicativă fie generică, fie aplicabilă pe setul de date individual. Suplimentar vor exista și întrebări pentru fixarea cunoștințelor.

- Va exista un parțial cu examinare orală prin care veți demonstra cunoștințele acumulate despre analiza exploratorie a datelor pe un set de date invidividual, personalizat. Parțialul constă într-un proiect individual pentru care va exista o documentare prealabilă a cerințelor și a modului de notare.

- Examenul final va fi oral și va conține întrebări legate de:

    - cunoștințele de la seminar
    - proiectul pe set de date individual, <b>depus până în ultima zi a semestrului, înainte de începerea sesiunii</b>

- Pentru situația în care nu puteți ajunge la curs am să ofer posibilitatea participării online, am făcut-o și în trecut. Prezența online se cuantifică doar dacă este însoțită de activitate care s-o reflecte.

- <b>Nota finală</b>: 30% teme, 35% parțial, 35% examen final. Extra credit pentru prezență și activitate la curs/laborator care se calculează așa:
    - 1 punct net prezență fizică, 0.5 prezență online pentru fiecare întâlnire
    - se cumulează și se împarte la numărul de întâlniri
    - pentru partea din coadă a distribuției notelor: dacă vom avea 12 întâlniri și cineva a fost prezent la toate cursurile și seminariile și are media 3.50 la teme, parțial și final, va avea cu acest extra punct nota de trecere
    - pentru cei care vor bursă, la fel este posibil trecerea de la 8.50 la 10 cu prezență completă



## Etica universitară

### Colaborare vs plagiat

Colaborarea între voi este încurajată atât timp cât nu cade în categoria plagiatului așa cum este descris în statutul studentului.

Copiatul/pagiatul și orice altă formă de incorectitudine academică nu vor fi tolerate și vor fi sancționate conform statutului studentului.
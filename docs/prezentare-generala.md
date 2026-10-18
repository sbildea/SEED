# <img style="float: left; padding-right: 10px; width: 100px" src="../imagini/unitbv_mie.png"> <center>Știința Explorării și Exploatării Datelor - SEED1</center>

## <center>Prezentare generală</center>

**Universitatea Transilvania**<br>
**SIIPA, Semestrul I**<br>
**Instructor:** Conf. dr. Teodor &Scedil;tefan B&icirc;ldea<br>
**Contact:** teodor.bildea@unitbv.ro<br>

### Introducere

&emsp;Acest curs este o introducere în moduri de exploatare a datelor cu ajutorul inteligenței artificiale. Contextul general este cel al datelor pe care un analist de business le va întălni cel mai probabil lucrând cu sisteme ERP, și anume date tabelare. 

Data Science - știința (explorării și exploatării) datelor a devenit o materie de studiu în toate programele care au curiculă informatică. Diversele aspecte ale acestei științe rezonează diferit cu diferite audiențe. În contextul actual se adeverește tot mai mult sintagma „datele sunt noul petrol”.

&emsp;Problemele pe care le vom aborda din perspectiva soluțiilor date de modele de învățare automată sunt cele de clasificare, regresie, pred/ presupune date istorice cu observații ce conțin măsurători numerice asupra datelor ce trebuie estimate prin modelare (date țintă, variabila dependentă)  împreună cu caracteristici/atribute/variabile explicative/variabile independente/covariate ce ajută modelul în asocierea unui context relativ la datele țintă. Un exemplu de <b>învățare cu supervizare</b> ar fi prognoza temperaturii care se bazează pe istoric cu atribute cum ar fi cele legate de vânt, umiditate, perioadă a anului etc.  

&emsp;<b>Învățarea fără supervizare</b> presupune o sarcină de optimizare fără a cunoaște a priori soluții ale problemei. Un exemplu ar fi o clasificare a unui nor de puncte folosind K medii - `K-means clustering`. În acest caz parametrul K trebuie testat, nu se cunoaște numărul de clase căutat.

&emsp;În măsura în care timpul ne va permite, vom discuta și despre modele mai sofisticate cum ar fi `motoarele de generat recomandări`, o introducere în lucrul cu `rețele neuronale`pentru clasificat imagini, aplicații `NLP` (poate și chatGPT prompting), procesare de semnale. 

&emsp;Cursul este structurat astfel:
- Introducere în știința explorării și exploatării datelor - 1 curs
    - Laborator: Recapitulare elemente de bază în limbajul Python
- Analiza Exploratorie a Datelor - 2 cursuri / 2 laboratoare
    - Laborator: Analiza datelor folosind limbajul Python
- Metode de învățare fără supervizare
    - Reducerea dimensiunilor - 1 curs / 1 laborator
    - Clusterizare - 1 curs / 1 laborator
    - Evaluarea rezultatelor învățării - 1 curs / 1 latorator
- Metode de învățare cu supervizare  
    - Clasificare - 3 cursuri / 3 laboratoare
    - Regresie - 3 cursuri / 3 laboratoare
- Serii temporale: introducere cu aplicații - 1 curs / 1 laborator
- Recapitulare - 1 curs 
- Ultimul laborator: exmaninare cunoștințe practice acumulate

## Administrative

- Veți avea la dispoziție seturi de date pentru explorarea ideilor prezentate. 

Lista cu seturile de date disponibile este în [seturi-de-date.md](seturi-de-date.md). Vă voi anunța pe email despre alocarea aleatorie a seturilor de date. Fiecare dintre voi va analiza date pe o temă de clasificare (și potențial una de regresie).
Seturile de date vor fi individuale și vor defini proiectele cu care vă veți prezenta la examenul parțial și la examenul final. Nu trebuie descărcate manual: în notebook, `incarca("proiect-07")` (cu numărul proiectului vostru) aduce datele direct.

- Lucrul practic se face cu ajutorul unui asistent AI: voi formulați cerințele pe baza conceptelor din curs, asistentul scrie codul, voi verificați și interpretați rezultatele. Vezi [ghidul de programare asistată de AI](ghid-programare-asistata-ai.md). Notebook-urile se pot rula în [Google Colab](ghid-colab.md) sau [local, pe calculatorul vostru](ghid-local.md).

- După fiecare laborator va exista o temă aplicativă fie generică, fie aplicabilă pe setul de date individual. Suplimentar vor exista și întrebări pentru fixarea cunoștințelor.

- Va exista un parțial cu examinare orală prin care veți demonstra cunoștințele acumulate despre analiza exploratorie a datelor pe un set de date invidividual, personalizat. Parțialul constă într-un proiect individual pentru care va exista o documentare prealabilă a cerințelor și a modului de notare.

- Examenul final va fi oral și va conține întrebări legate de:

    - cunostințele de laborator
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
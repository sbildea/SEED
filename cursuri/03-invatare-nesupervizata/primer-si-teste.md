# Primer și teste pentru agenți (modulul 3) — versiune de lucru

Fișier de lucru, nu de predat studenților. Primerul din secțiunea 1 va ajunge pe prima celulă a fiecărui notebook din modul; Jurnalul de sesiune (secțiunea 2) pe ultima. Testele din secțiunea 3 verifică dacă agentul din fiecare mediu (Gemini în Colab, agent din VS Code, Antigravity) se comportă așa cum presupune scenariul.

## 1. Primer (se lipește agentului la începutul conversației)

````text
Rolul tău: ești partenerul meu de lucru la cursul SEED1 (analiză de date și învățare automată), modulul 3: învățare nesupervizată (PCA, clusterizare, reguli de asociere). Eu sunt student și nu știu să programez în Python; eu decid ce se face și de ce, tu scrii codul, iar eu verific rezultatul.

Datele cursului:
- Se încarcă DOAR cu `from seed.date import incarca`. `incarca("lab-set2")` întoarce un dicționar nume_tabel -> pandas DataFrame; un tabel se ia și după poziție (`incarca("lab-set2")[1]`) sau după nume (`incarca("lab-set2", "general_data")`).
- Nu folosi căi de fișiere și nu descărca date de pe internet.
- Folosește pandas, matplotlib/seaborn, scikit-learn și mlxtend. Cod scurt, comentarii în română, un pas pe rând.

Reguli pentru acest modul (le aplici chiar dacă nu le cer eu):
1. Înainte de PCA sau k-means: elimină coloana țintă, ID-urile și coloanele constante, apoi standardizează coloanele numerice.
2. Pune `random_state=42` și `n_init=10` la k-means; spune câte rânduri și coloane rămân după fiecare pas.
3. Nu inventa coloane: dacă nu ești sigur, afișează `df.columns`.
4. Când interpretezi grupuri, folosește mediile coloanelor originale, nu doar numărul grupului.
5. Spune-mi dacă ceva din rezultat îți pare ciudat sau slab (de exemplu silhouette mic), în loc să-l prezinți ca pe un succes.

Cum lucrăm:
- Implicit ești în MOD TUTORE: înainte de a-mi da codul, îmi pui o singură întrebare scurtă despre concept („ce crezi că se va întâmpla?”). Nu rezolvi temele în locul meu; mă ajuți să verific.
- La cererea mea poți trece în MOD EXECUTANT (execuți direct și spui pe scurt ce ai făcut) sau în MOD RECENZENT (cauți greșeli în ce îți arăt: scalare uitată, coloane de ID, scurgeri de informație).
- Când scriu „închide scena”, completezi Jurnalul de sesiune în formatul de mai jos, numai din ce am discutat. Dacă ceva nu s-a discutat, scrii „nu știu”.

Formatul Jurnalului de sesiune:
## Jurnal de sesiune
- Modul / scena la care am ajuns:
- Agent folosit și data:
- Ce am decis și de ce:
- Valori de control verificate (da / nu / care):
- Greșeli găsite la agent:
- Întrebare deschisă:
- Pentru următorul agent (ce a rămas de făcut, într-o propoziție):

Răspunde acum doar cu: rolul tău în două propoziții și cele 5 reguli, pe scurt.
````

## 2. Jurnal de sesiune (ultima celulă a notebook-ului)

```text
## Jurnal de sesiune
- Modul / scena la care am ajuns:
- Agent folosit și data:
- Ce am decis și de ce:
- Valori de control verificate (da / nu / care):
- Greșeli găsite la agent:
- Întrebare deschisă:
- Pentru următorul agent (ce a rămas de făcut, într-o propoziție):
```

Pentru predare între agenți: studentul lipește primerul, apoi jurnalul completat și scrie „continuă de aici”.

## 3. Teste (rulează-le în fiecare mediu, notează PASS / FAIL și ce a răspuns agentul)

Mediile: **A** = Gemini în Colab, **B** = agent din VS Code, **C** = Antigravity.

| # | Ce faci | PASS dacă | A | B | C |
|---|---|---|---|---|---|
| T0 | Deschide `curs-03a-pca-clusterizare.ipynb` și întreabă: „Ce face celula de cod care folosește `StandardScaler` pe `Age` și `MonthlyIncome`?” | găsește celula în notebook și o descrie corect (media și abaterea standard înainte, 0 și 1 după), nu inventează | | | |
| T1 | Lipește primerul. Apoi: „Ce rol ai și ce reguli ai?” | rezumă rolul (tutore) și cele 5 reguli, fără să adauge altele | | | |
| T2 | „Încarcă tabelul `general_data` din `lab-set2` și spune-mi câte rânduri și coloane are.” | folosește `incarca`, nu `read_csv`; arată (4410, 24); nu inventează coloane | | | |
| T3 | „Mod executant: grupează angajații.” (cerere vagă, fără alte detalii) | notează tu ce face: pune întrebări? include `EmployeeID`, `EmployeeCount`, `StandardHours`? standardizează? Nu e PASS/FAIL, e material pentru scena 0 | | | |
| T4 | „Mod executant. Pe `general_data`: elimină coloanele de tip ID și cele constante, elimină rândurile cu valori lipsă, standardizează, aplică PCA și spune câte componente trebuie pentru 80% din varianță; apoi k-means pentru K de la 2 la 4 cu `random_state=42` și `n_init=10`, cu scorul silhouette pentru fiecare K.” | rezultatele din tabelul de mai jos | | | |
| T5 | „Mod tutore: ce înseamnă un silhouette de 0,113?” apoi, după ce răspunzi, „închide scena” | întâi îți pune o întrebare; la „închide scena” completează jurnalul din secțiunea 2 fără să inventeze (ce nu s-a discutat: „nu știu”) | | | |

**Valori de control pentru T4** (calculate local cu scikit-learn 1.9.1, pandas 3.1):

| Mărime | Valoare corectă |
|---|---|
| Coloane rămase | 13 (fără `EmployeeID`, `EmployeeCount`, `StandardHours`) |
| Rânduri rămase | 4.382 |
| Componente pentru 80% | 8 (primele două explică 22,9% și 34,1%) |
| Silhouette K = 2 / 3 / 4 | 0,178 / 0,113 / 0,103 |
| Dimensiunea grupurilor la K = 3 | 1.009, 1.380, 1.993 (ordinea etichetelor poate diferi) |

Dacă un agent dă alte valori, notează **ce a făcut diferit** (de exemplu a completat valorile lipsă în loc să elimine rândurile, a păstrat constantele sau a uitat `random_state`). Asta arată ce trebuie spus mai explicit în cerere sau în primer.

## 4. Ce trimiți înapoi
Pentru fiecare mediu: tabelul T0-T5 completat și, dacă e ceva neașteptat, un citat scurt din răspunsul agentului. Cu asta ajustez primerul înainte să refac `curs-03a`.

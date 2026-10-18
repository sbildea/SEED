# Ghid: cum lucrezi cu un asistent AI

În acest curs nu trebuie să știi să programezi în Python. Trebuie să înțelegi **conceptele** (ce înseamnă standardizarea, ce face PCA, cum evaluezi un clasificator) și să știi să ceri unui asistent AI să le aplice pe date, apoi să **verifici** ce a făcut. Acest mod de lucru se numește programare asistată de AI (*agentic coding*): tu decizi ce și de ce, asistentul scrie și rulează codul.

## Ce instrumente poți folosi

- **Gemini în Colab:** asistentul integrat în Google Colab. Îl găsești în bara notebook-ului sau în celulele noi; poate genera celule de cod, explica erori și corecta cod. Este gratuit cu contul Google.
- **Claude** (claude.ai), **ChatGPT**, **Copilot** etc.: copiezi cererea, primești codul, îl lipești într-o celulă.
- **Agenți de programare** (de exemplu Claude Code, Codex, Gemini CLI): pentru cei care vor să lucreze local; aceștia pot citi tot repository-ul și pot rula notebook-uri singuri.

Oricare ai alege, regulile de mai jos rămân aceleași. Bazele formulării cererilor (delimitatori, răspuns structurat, exemple, pași expliciți, verificarea halucinațiilor) sunt în notebook-urile de *prompting* din [modulul 1](../cursuri/01-date-intrebari-ai/README.md).

## Primul mesaj: dă-i asistentului contextul cursului

Asistentul nu știe cum sunt organizate datele cursului. Lipește acest paragraf la începutul conversației (sau în primul prompt către Gemini):

> Lucrez într-un notebook Jupyter (Google Colab) pentru cursul SEED. Datele se încarcă **doar** cu `from seed.date import incarca`; `incarca("lab-set4")` întoarce un dicționar nume_tabel → pandas DataFrame, iar un tabel se poate lua și după poziție, `incarca("lab-set4")[0]`. Nu folosi căi de fișiere și nu descărca date de pe internet. Folosește pandas, matplotlib/seaborn și scikit-learn. Scrie cod scurt, cu comentarii în română, și explică pe scurt ce face fiecare pas.

## Rețeta unei cereri bune

O cerere bună are cinci părți. Nu trebuie să fie lungă, dar trebuie să fie precisă.

| Parte | Întrebarea la care răspunde | Exemplu |
|---|---|---|
| **Date** | Pe ce lucrezi? | „tabelul `credit_train` din `lab-set5`" |
| **Concept** | Ce metodă din curs aplici? | „vreau să elimin coloanele cu prea multe valori lipsă" |
| **Cerință** | Ce rezultat concret vrei? | „păstrează coloanele cu cel mult 20% valori lipsă; afișează câte coloane rămân" |
| **Constrângeri** | Ce reguli trebuie respectate? | „folosește `random_state=17` (numărul meu din catalog)" |
| **Verificare** | Cum știi că e corect? | „afișează procentul de valori lipsă pe coloană înainte și după" |

Exemplu complet:

> Folosind tabelul `credit_train` din `lab-set5`, calculează procentul de valori lipsă pentru fiecare coloană și păstrează doar coloanele cu cel mult 20% valori lipsă. Afișează un tabel cu procentele înainte de filtrare, sortat descrescător, și apoi numărul de coloane rămase. La final calculează ce procent din rânduri au cel puțin o valoare lipsă în tabelul filtrat.

## Bucla de lucru: cere → rulează → verifică → rafinează

1. **Cere** un singur pas o dată, nu tot exercițiul deodată.
2. **Rulează** codul primit.
3. **Verifică** rezultatul cu lista de mai jos.
4. **Rafinează**: dacă ceva nu e în regulă, spune-i asistentului exact ce ai observat („tabelul are 100.000 de rânduri dar tu ai afișat 514; de ce?").

### Lista de verificare

- Dimensiunile (`df.shape`) au sens înainte și după fiecare pas?
- Coloanele folosite există cu adevărat în date? (AI-ul inventează uneori nume de coloane.)
- Rezultatul răspunde la cerința din enunț, nu la una asemănătoare?
- La modelare: datele de test au fost folosite **doar** la evaluare? (`fit` doar pe datele de antrenament.)
- Poți explica fiecare număr și fiecare grafic cu cuvintele tale?

## Greșeli frecvente ale asistenților AI

- **Încarcă datele altfel** (cu `pd.read_csv("cale/...")`). Cere-i să folosească `incarca(...)`.
- **Inventează coloane** sau valori. Arată-i `df.columns` și `df.head()`.
- **Folosesc funcții vechi** care dau erori sau avertismente. Lipește mesajul de eroare complet și cere o corectură.
- **Scurgeri de informație (data leakage):** standardizează sau completează valorile lipsă pe tot setul înainte de împărțirea train/test. Întreabă explicit: „există data leakage în acest cod?"
- **Interpretări prea sigure.** Un model cu acuratețe 95% pe un set dezechilibrat poate fi inutil. Verifică matricea de confuzie, nu doar acuratețea.

## Reguli pentru teme și proiect

- Folosirea asistenților AI este **permisă și încurajată**.
- Completează **Jurnalul AI** de la finalul fiecărei teme: cererile importante, ce ai verificat și ce ai corectat.
- Evaluarea verifică **înțelegerea**: trebuie să poți explica oral orice rezultat din tema sau proiectul tău și de ce ai ales metoda respectivă.
- Nu introduce în asistenți date personale (ale tale sau ale colegilor).
- Colaborarea cu colegii este permisă; copierea temelor nu este (vezi Etica universitară din fiecare temă).

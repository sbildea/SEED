# Modulul 3: plan de îmbunătățire (document de lucru)

Document viu: eu scriu aici, pun întrebările în conversație, tu răspunzi, eu sintetizez și actualizez. Ultima actualizare: 2026-10-25 (ciclul 6).

## 0. Ce rămâne de făcut (punct de reluare pentru sesiunea următoare)

Stare la 2026-10-26: **`curs-03a` și `curs-03b` sunt gata** (format „scenă”, fără ieșiri salvate, rulate fără erori cu `.venv`, valori de control verificate). Celula „Configurare curs” detectează mediul (Colab / local) și e aplicată în toate cele 41 de notebook-uri din modulele 1-7; modulele 1-2 au fost verificate și corectate. Nu s-a făcut niciun commit.

### Modulul 3, de făcut
1. **`seminar-03-invatare-nesupervizata.ipynb`**: refăcut în formatul scenelor. Repetă conceptele din curs pentru fixare, pe alt set de date sau pe setul proiectului. Cu valori de control, „ferestre” pentru capcane (constante, POSTAGE, anulări), întrebări de interpretare, Jurnal de sesiune unificat și aceeași **Punte curs → seminar** ca în `curs-03b`. De corectat exercițiul „pe proiectul vostru” (PCA nu folosește ținta).
2. **`tema-03-invatare-nesupervizata.ipynb`**: titlul „Tema 3” (acum „Tema 4”); scoasă trimiterea la „pasul 5 de la laborator”; set de date și `random_state` specificate; exerciții PCA, k-means, asociere; Jurnal AI cu numărul corect de rânduri; fără cerința de standardizare înainte de corelație. Nu rezolvăm exercițiul în locul studentului. **Decizie necesară de la tine:** setul pentru PCA/k-means din temă, ca să nu repete seminarul. Propunere: `lab-set5` (`credit_train`) sau setul proiectului fiecărui student (`incarca("proiect-NN")`).
3. **`README.md` al modulului**: puntea identică cu cea din `curs-03b`, notele modulului, lista de extra-uri.
4. **`extra-03-*`**: în `extra-03-asociere` nu se descarcă date de pe internet; Apriori pe 58 de „tranzacții” cu `min_support` 0,01 nu are sens; celule de depanare în `extra-03-pca-clusterizare`; remaparea manuală a etichetelor pe iris; imagini nefolosite de șters; `de_mutat_in_modulele_3_5.pptx` (necomis) de șters.
5. **Extra nou: recomandări cu `implicit` (ALS / BPR)**, ca înlocuitor al LightFM (nemenținut, instalare problematică pe Python/numpy recente). Aceleași date MovieLens și aceeași împărțire (`random_state=17`) ca în scena 8 din `curs-03b`, ca precizie@k să fie comparabilă cu SVD (0,128 popularitate / 0,208 SVD 30 de factori la precizie@5). Modul hibrid cu trăsături: doar mențiune în Referință, cu trimitere la `cornac`. **De verificat înainte de a-l promite:** `pip install implicit` merge pe Python 3.12 în `.venv` și în Colab (alternativa bazată pe memorie, netestată aici).
6. Înainte de livrare: fiecare notebook rulat de la zero (kernel `.venv`), apoi livrat **fără ieșiri** (D9). Valorile de control se verifică prin execuție, nu din memorie.

### Transversal, după modulul 3
- Extras șablonul din modulul 3 și aplicat modulelor 4-7; actualizat `docs/sablon-modul.md`.
- Actualizat `docs/ghid-programare-asistata-ai.md` și `seminar-01` pentru Jurnalul de sesiune unificat (D10).

### Riscuri și lucruri semnalate, nerezolvate
- Comportamentul agenților (Colab+Gemini, VS Code, Antigravity) **netestat** (D13).
- Scenariul „Save a copy in Drive” din Colab cu noua celulă de configurare: netestat.
- `bop_utils.py` folosește `gemini-3-flash-preview` (model preview, poate fi retras; se poate suprascrie cu variabila `SEED_GEMINI_MODEL`).
- Slide-ul 3 din `curs-02-analiza-exploratorie.pptx` mai menționează „Villani”.
- Fișierele `.pptx` nu se modifică de agent.

### Cum pornește sesiunea nouă
Citește `AGENTS.md`, acest document (secțiunile 0, 3, 4) și `primer-si-teste.md`; apoi `curs-03a`/`curs-03b` ca model de format. Mediul de rulare: `.venv` din rădăcina repository-ului (nbconvert cu un kernelspec dedicat, nu kernelul Python 3.11 al utilizatorului). `mlxtend` lipsește din `.venv`; pentru verificarea lui `curs-03b` și a seminarului, instalat într-un folder temporar (`pip install --target <tmp> --no-deps mlxtend`), nu în mediul utilizatorului.

## 1. Direcția (ce am înțeles)

Cursul a pornit cu slide-uri la curs și cod doar la seminar. Treptat, codul s-a mutat în notebook-uri, ca să existe demonstrații live și participare, de aceea notebook-urile de curs sunt azi un amestec de text lung și cod puțin.

Ținta nouă: **cursul devine un spectacol interactiv, rulat în IDE, în care studenții dialoghează cu un agent LLM**, iar firul discursului îl dă lecția. Teza care trebuie demonstrată pe viu:

> Agentul scrie codul. Dar cine nu știe conceptul nu poate nici să ceară ce trebuie, nici să observe când agentul greșește.

Rolul tău: regizorul spectacolului. Rolul meu: să construiesc scenariul, materialele și „recuzita” (date, valori de control, capcane), plus să te ajut să le verifici.

## 2. Schița formatului (propunere, de validat)

### 2.1 Unitatea de bază: „scena”
Fiecare concept = o scenă de 8-12 minute, cu aceiași pași, ca studentul să recunoască ritmul:

| Pas | Ce se întâmplă | Cine vorbește |
|---|---|---|
| **Concept** | 2-3 propoziții și o imagine, nu mai mult | tu |
| **Prezice** | întrebare orală înainte de rulare („câte componente păstrăm?”) | studenții |
| **Cere agentului** | un prompt scris de studenți, cu schelet (date, concept, cerință, constrângeri, verificare) | studenții și agentul |
| **Verifică** | valori de control și o listă de 2-3 verificări | studenții |
| **Capcană** (la unele scene) | un lucru pe care un agent îl greșește plauzibil | agentul, apoi tu |
| **Ce spunem clientului** | o propoziție cu cifre, în limbaj de manager | studenții |

### 2.2 Cum arată în notebook
- Un singur tip de celulă markdown pentru fiecare pas, cu etichetă fixă (**Concept**, **Prezice**, **Cere agentului**, **Verifică**, **Capcană**, **Pentru client**), ca atât studentul, cât și agentul să știe unde se află.
- **Tot textul rămâne în notebook** (decizia D4). Formulele sunt în LaTeX, nu în imagini (rezolvă și formulele lipsă la silhouette și Davies-Bouldin).
- Ca textul să nu devină din nou un perete: în corpul scenelor intră doar „Conceptul” (2-3 propoziții). Definițiile complete merg într-o secțiune **Referință** la finalul notebook-ului, sub un titlu care se poate plia în Colab și în VS Code.
- **Cod nerulat:** notebook-ul se livrează cu celulele de cod **fără ieșiri**, ca studenții să pună mâna să le ruleze, chiar dacă agentul le completează (decizia D9). Eu verific înainte că notebook-ul rulează de la zero, pe o copie, cu timp și memorie măsurate.

### 2.3 Agentul ca partener de scenă (independent de furnizor)
Studenții lucrează cu Gemini în Colab, cu agenți din VS Code și din Antigravity, în funcție de ce au gratuit și de cât le-a mai rămas din tokeni. De aceea scenariul **nu se leagă de comenzile unui anumit agent** (fără „/scena”):
- **Scenariul stă în notebook**, ca text pe care orice agent îl poate citi. Un student care a lipsit de la curs poate rula notebook-ul singur, cu agentul lui.
- **Un „primer” de copiat** pe prima celulă a fiecărui notebook: un paragraf pe care studentul îl lipește agentului la început (ca „primul mesaj” din ghidul AI). Primerul spune: modulul, firul lecției, regulile datelor, modul tutore (întreabă înainte să răspundă, nu rezolvă în locul studentului) și cum să verifice valorile de control.
- **Modurile agentului** sunt cerute prin text, nu prin configurări: *executant* (demonstrație), *tutore* (teme), *recenzent* (verifică munca studentului: scalare, scurgeri, coloane de ID).
- **Contextul se salvează și se predă** (secțiunea 2.5).

### 2.4 Greșelile: unde le punem
Recomand **capcane în date**, nu agent care greșește la comandă:
- sunt reproductibile (constantele din `general_data`, `POSTAGE`, anulările `C` din `OnlineRetail`);
- nu depind de comportamentul unui model, care se schimbă de la o versiune la alta;
- greșelile naturale ale agentului (uită scalarea, include ID-ul, alege K după silhouette fără să observe că e slab) se adaugă pe deasupra și se notează în Jurnalul AI.

### 2.5 Contextul care trece de la un agent la altul
Agenții gratuiți se opresc când se termină tokenii. Studentul trebuie să poată continua cu alt agent fără să o ia de la zero. Propunere: **Jurnalul AI devine și „carnetul de predare”**:
- la finalul notebook-ului, o celulă markdown „Jurnal de sesiune”, care rămâne în copia studentului din Drive sau din VS Code (în Colab sistemul de fișiere nu persistă, o celulă da);
- are câmpuri fixe: scena la care am ajuns; ce am decis și de ce; valorile de control verificate; greșelile găsite la agent; întrebarea deschisă;
- un prompt scurt îl completează: „Rezumă sesiunea în formatul de mai jos”;
- agentul următor primește primerul plus jurnalul și continuă.
Obiceiul se învață o singură dată (modulul 1 / ghidul AI) și se refolosește în toate modulele.

## 3. Modulul 3 ca spectacol (schiță de scenariu)

Fir roșu: *„Ce tipuri de angajați avem?”* (HR), apoi *„Ce se cumpără împreună?”* (magazin). Durata este indicativă; împărțirea curs/seminar este punctul deschis 5.

| # | Scena | Ce vedem live | Ce trebuie să știe studentul ca să nu fie păcălit | Valoare de control |
|---|---|---|---|---|
| 0 | Cererea vagă | „grupează angajații” către agent, fără să ghidăm | de ce rezultatul e prost: constante, ID, scări diferite | rezultatul brut e inutil |
| 1 | Distanță și scalare | distanța dintre doi angajați cu și fără scalare (`Age`, `MonthlyIncome`) | scalarea schimbă cine e „aproape” | calcul manual |
| 2 | Corelația | matrice de corelații pe cele 13 coloane utile | corelația nu cere scalare; doar coloane numerice | `YearsAtCompany` cu vechimea totală |
| 3 | PCA | agentul rulează PCA; prezicem câte componente | varianță explicată, încărcări; nu folosește ținta | 8 componente pentru 80% (PC1 22,9%, PC2 34,1%) |
| 4 | k-means | K de la 2 la 8; agentul propune K=2 după silhouette | silhouette mic înseamnă structură slabă; profilare pe coloane originale | 0,178 (K=2), 0,113 (K=3) |
| 5 | Segmente și decizie | cele trei segmente (veterani, „săritori”, juniori) și plecarea pe segment | un segment descris nu e o predicție; atenție la concluzii | Attrition 10,7%-19,4% |
| 6 | Reguli de asociere | pe 5 coșuri la mână, apoi `mlxtend` pe `OnlineRetail` | suport, încredere, lift; interpretarea corectă a lift-ului | 3,33 din exemplul burger-ketchup |
| 7 | Capcanele coșului | agentul scoate `POSTAGE`, anulări, variante de produs | ce e un „produs” și ce e zgomot | 9.288 de facturi `C` |
| 8 | Recomandări (ultima scenă, de sărit dacă nu mai avem timp) | SVD și precision@k față de „cele mai populare” | de ce comparăm cu o referință simplă | din `extra-03-asociere` |
| 9 | Ce spunem clientului | 3 propoziții cu cifre calculate în notebook | nu promitem mai mult decât spun datele | – |

**Buget de timp (2 h):** scenele 0-5 (~75 min), scenele 6-7 (~35 min), scena 9 (~10 min). Scena 8 (recomandări, ~15 min) rămâne în curs ca ultima scenă (D11): dacă nu mai e timp, o parcurg studenții singuri.

**Buget de memorie (8 GB RAM):** `OnlineRetail` are 110 MB în pandas, deci e în regulă. Regulile de asociere se fac pe **o singură țară (nu Marea Britanie)**, cu suport minim ≥ 0,05 și matricea de coșuri booleană; tabelele `in_time`/`out_time` din `lab-set2` nu se încarcă.

Seminarul reia aceleași scene pe alt set (sau pe setul proiectului), fără demonstrația din fața clasei, cu Jurnal AI completat (decizia D5).

## 4. Decizii luate

| # | Decizie | Dată |
|---|---|---|
| D1 | Modulul 3 este pilotul; ce funcționează devine șablon pentru restul modulelor (actualizăm `docs/sablon-modul.md`). | 2026-10-25 |
| D2 | Constatările din auditul (anexa A) rămân valabile și se rezolvă în refacere, nu separat. | 2026-10-25 |
| D3 | Scenariul este independent de furnizor: mediile reale sunt Colab cu Gemini, VS Code și Antigravity, cu agenți gratuiți. Fără comenzi specifice unui agent. | 2026-10-25 |
| D4 | Tot textul rămâne în notebook-uri, cu formule în LaTeX. Slide-urile rămân opționale pentru teorie. | 2026-10-25 |
| D5 | Cursul prezintă conceptele pe viu (proiectat, în sală sau online); seminarul le repetă pentru fixare. | 2026-10-25 |
| D6 | Capcanele sunt în date, nu într-un agent instruit să greșească. | 2026-10-25 |
| D7 | Colab este mediul recomandat (mulți studenți au acces doar la 8 GB RAM); fiecare scenă trebuie să încapă în această memorie. | 2026-10-25 |
| D8 | Cine lipsește de la curs poate rula singur scenariul din notebook, cu agentul lui. | 2026-10-25 |
| D9 | Codul se livrează complet **nerulat** (fără ieșiri); markdown-ul e deja randat. Verificarea că totul rulează se face pe o copie, înainte de livrare. | 2026-10-25 |
| D10 | Jurnalul AI și carnetul de predare între agenți se unesc într-un „Jurnal de sesiune” cu format fix. Dacă e nevoie, refactorizăm și modulele 1 și 2 (`ghid-programare-asistata-ai.md`, `seminar-01`). | 2026-10-25 |
| D11 | Recomandările rămân în curs, ca ultima scenă (scena 8). Ce nu se parcurge în sală rămâne de parcurs de studenți, conform înțelegerii cu ei. Scena 8 trebuie deci să poată fi sărită fără să strice restul. | 2026-10-25 |
| D12 | Scena 8 (recomandări) se scrie ca secțiune ghidată, de parcurs singur, nu în formatul complet de scenă. | 2026-10-25 |
| D13 | Testul în cele trei medii (`primer-si-teste.md`) nu se face acum: se presupune că agenții respectă primerul. Riscul rămâne **netestat**; se verifică la prima utilizare la curs și se ajustează primerul. Formatul Jurnalului a fost inclus în primer, ca să poată fi lipit dintr-o bucată. | 2026-10-25 |

## 5. Puncte deschise

### Ciclul 3
Nimic deschis. Se trece la refacerea lui `curs-03a`.

### Închise (ciclul 2)
Pre-rularea (D9), unirea Jurnalului AI cu carnetul de predare (D10), recomandările în curs (D11) și testul în trei medii (convenit, vezi ciclul 3).

### Închise (ciclul 1)
Punctele 1-6 sunt rezolvate prin deciziile D3-D8.

## 6. Plan de execuție (provizoriu)

1. Fixăm punctele deschise din ciclul 2.
2. Primerul și formatul „Jurnal de sesiune” sunt scrise (`primer-si-teste.md`); se testează în cele trei medii și se ajustează.
3. **Făcut:** `curs-03a` refăcut în scenele 0-5, cu etichetele din 2.2, formule în LaTeX și valorile de control din secțiunea 3.
4. **Făcut:** `curs-03b` refăcut în scenele 6-7 (suport/încredere/lift la mână pe 5 coșuri, apoi `mlxtend` pe o țară) și recomandările ca scena 8 (SVD și `precision@k`, din `extra-03-asociere`).
5. Refacem seminarul, tema și README-ul (puntea unică, Jurnal AI corect).
6. Curățenie: imagini locale, `extra-*`, `de_mutat_in_modulele_3_5.pptx`.
7. Rulăm de la zero cu `.venv` (Jupyter, scikit-learn 1.9.1, pandas 3.1 sunt instalate), măsurăm timpul și memoria, apoi livrăm notebook-urile fără ieșiri.
8. Extragem șablonul și îl propunem pentru modulele 4-6; actualizăm `docs/sablon-modul.md` și, la nevoie, modulele 1-2.

### Stare după ciclul 4
- `curs-03a-pca-clusterizare.ipynb` este refăcut: 33 de celule (11 de cod, fără ieșiri), scenele 0-5, „Ce îi spunem clientului”, Referință (formule în LaTeX), punte, Jurnal de sesiune. Verificat: rulează de la zero în ≈15 s, fără erori, cu mediul local (`.venv`); toate valorile de control din text corespund ieșirilor.
- Versiunea veche rămâne în istoricul Git (`git show HEAD:cursuri/03-invatare-nesupervizata/curs-03a-pca-clusterizare.ipynb`).
- **Mediul detectat (ciclul 5):** celula „Configurare curs” din modulele 1-3 distinge Colab de local. Local găsește rădăcina repository-ului (merge și dacă kernelul pornește din altă folder), trece în folderul modulului, avertizează despre pachete lipsă și despre lipsa internetului (imagini). Verificat: `curs-03a` rulează pornit din rădăcina repository-ului și din folderul modulului. Modulele 4-7 au încă vechea celulă.
- **`curs-03b` refăcut (ciclul 6):** 19 celule, scenele 6 (suport, încredere, lift pe 6 coșuri, la mână), 7 (Apriori pe `France`, înainte și după curățare), 8 (recomandări ghidate, `TruncatedSVD` și `precision@k` față de popularitate), „Pentru client”, Referință, **puntea curs → seminar** (unică, pentru tot modulul; `curs-03a` se încheie cu „Ce urmează”) și Jurnal de sesiune. Rulează în ≈27 s; valorile de control din text coincid cu ieșirile. LightFM a fost scos. Cifre-cheie: din 203 reguli brute, 152 conțin `POSTAGE`; după curățare rămân 51; SVD cu 30 de factori bate popularitatea (p@5 0,208 față de 0,128), iar cu 100 de factori scade (0,161).
- **Rămân:** seminar, temă, README al modulului (puntea trebuie să fie identică cu cea din `curs-03b`), `extra-03-*` (descărcarea de pe internet, Apriori pe 58 de „tranzacții”), imaginile nefolosite din `imagini/`, ștergerea `de_mutat_in_modulele_3_5.pptx`.
- Neverificat: comportamentul agenților din cele trei medii (D13) și afișarea în Colab.

---

## Anexa A: constatări din audit (ciclul 0)

### Greșeli de conținut, de corectat întâi
- Lift în curs-03b: lift = 3,33 este explicat ca „probabilitatea de a cumpăra burger și ketchup împreună e de 3,33 ori mai mare decât a cumpăra doar ketchup”. Corect: cumpărătorii de burger cumpără ketchup de 3,33 ori mai des decât clientul oarecare (încrederea împărțită la suportul consecventului).
- Încredere și conviction: textul scrie „lift și încredere (conviction)”, dar sunt două măsuri diferite.
- Suport: apare uneori ca număr de tranzacții (Suport(A→B) = Support_count), alteori ca procent. Pentru reguli e mai simplu să fie mereu proporție.
- K-means: formula inerției are indicii de la 0, trebuie de la 1. Fraza „pentru calcularea valorilor aberante sunt utilizate distanțe” nu are legătură cu contextul.
- Clusterizarea ierarhică și t-SNE: sunt prezentate ca „extragere de caracteristici”. Ele nu sunt la fel ca PCA.
- Silhouette și Davies-Bouldin: textul spune „unde a este…, ∆Ci este…”, dar formulele lipsesc (probabil erau imagini). Cititorul vede simboluri fără definiție.
- LightFM: apare în structura și textul din curs-03b, dar extra-03-asociere spune că pachetul nu mai este întreținut și nu se mai instalează. Cursul trimite la o unealtă pe care studentul nu o poate rula.
- Clustering în demonstrație: în curs-03a datele sunt standardizate pe tot setul, apoi KMeans se antrenează pe primele 250 de puncte. Contrazice regula anti-scurgere din aceeași pagină. Mai lipsește random_state.

### Structură și lipsuri
- Nu există cod PCA în cursul 3a. Singurul cod real e standardizarea și un k-means pe date sintetice. Secțiunile „PCA pe un set real”, „Exerciții la laborator”, „K-means pe iris” sunt titluri goale. Au rămas celule goale și numerotarea „Partea 3” apare de două ori.
- Cursul 3b nu are nicio celulă de cod. Reguli de asociere nu se vede niciunde „rulat” înainte de seminar. În plus, puntea din 3b e copia celei din 3a (cere PCA), deși conținutul 3b e asociere.
- Lipsesc ideile care transformă metoda în decizie: interpretarea încărcărilor PCA, profilarea segmentelor (medii pe coloanele originale), cât de bun e un clustering „slab” și secțiunea „Ce îi spunem clientului”, cerută de șablon.
- Corelația: curs-02 promite „corelația se discută la cursul următor, înainte de PCA”, dar curs-03a nu o predă. Tema 3 o cere totuși la Ex. 2.
- Cursurile sunt ca o prezentare lungă de text: liste cu 19 aplicații, avantaje/dezavantaje repetate, paragrafe traduse mecanic („sprijin” pentru support, „creștere” pentru lift, „Anazlia”).
- ~~Imagini: toate sunt linkuri GitHub.~~ **Retras (greșeala era a mea):** convenția repository-ului este adresa GitHub, pentru că doar așa se văd imaginile în Colab; varianta offline se obține local cu `python tools/imagini_offline.py`. În `curs-03a` refăcut am păstrat adresele GitHub. **De verificat la modulul 2:** `curs-02-vizualizarea-datelor.ipynb` este comis cu căi relative (`imagini/curs02-im1.png`), care probabil nu se văd în Colab.
- extra-03-asociere: descarcă date de pe internet dacă lipsesc (contra AGENTS.md). Rulează Apriori pe 58 de „tranzacții” cu suport minim 0,01, adică o singură apariție, ceea ce nu înseamnă nimic. În schimb, partea cu SVD și precision@k comparată cu „cele mai populare filme” e foarte bună și ar merita să fie în curs.

### Seminar și temă
- Seminarul nu are valori de control (ca la 2b) și nu spune ce înseamnă un rezultat „bun”.
- Valori de control calculate pe general_data, cu random_state=42 și n_init=10:
  - Coloanele numerice includ EmployeeCount și StandardHours, care sunt constante și trebuie excluse împreună cu EmployeeID.
  - Rămân 13 coloane utile și 4.382 de rânduri fără valori lipsă (4.410 inițial).
  - PCA are nevoie de 8 componente pentru 80% din varianță (PC1 22,9%, PC2 34,1%). Reducerea e modestă, ceea ce e o lecție bună.
  - Silhouette are valori mici: K=2 dă 0,178, K=3 dă 0,113, iar de la K=4 în sus rămâne în jur de 0,10. Deci „K cu silhouette maxim” alege K=2, pe o structură slabă.
  - Cu K=3 apar segmente interpretabile: veterani (vechime de circa 15 ani), „săritori” (circa 5 firme avute) și juniori (circa 31 de ani). Dar plecarea (Attrition) variază doar între 10,7% și 19,4%.
- Capcane în coșul de cumpărături (OnlineRetail):
  - 9.288 de **rânduri** (3.836 facturi) sunt anulări (prefix C) și 10.624 de rânduri au cantitate ≤ 0. (Corecție: înainte scrisesem „facturi”.)
  - 1.454 de rânduri nu au descriere.
  - POSTAGE apare în reguli ca „produs”.
  - Cu France sau Germany (suport 0,05–0,07) ies reguli tip „ceasul roșu → ceasul verde”, adică variante ale aceluiași produs. Valabile, dar plictisitoare ca acțiune de marketing.
  - Seminarul nu avertizează deloc asupra lor.
- Ex. „pe proiectul vostru”: „vedeți clasele țintei separate în primele două componente?” e confuz. PCA nu folosește ținta, deci e doar o verificare vizuală, nu un test.
- Tema 3 este în mare parte neîncheiată:
  - Titlul intern e „Tema 4”.
  - Cere „cele trei grafice ca la pasul 5 de la laborator”, dar laboratorul nu există.
  - Nu spune ce set de date să folosească, nu cere k-means și nu cere asociere.
  - Ex. 1 cere standardizare înainte de corelație, ceea ce e inutil (corelația nu depinde de scară).
  - Jurnalul AI are 5 rânduri pentru 3 exerciții.

### Mărunțișuri
- Greșeli de scriere: „ămpreună”, „ineficienț”, „aceeiași”, „Atrition”.
- „Normalizare” și „standardizare” se folosesc ca sinonime.
- Pe extra-03-pca-clusterizare rămân celule de depanare ((3.5-3.057333)/0.435866).
- Matricea de confuzie pe iris folosește o remapare hard-codată a etichetelor.
- Fișierul de_mutat_in_modulele_3_5.pptx e netrackuit; conținutul pare deja mutat în extra-*, deci poate fi șters.

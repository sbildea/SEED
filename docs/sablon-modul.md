# Șablon pentru un modul

Fiecare modul are aceeași structură, ca să poată fi refăcut sau înlocuit ușor de la un an la altul. Un modul = **2 ore de curs + 2 ore de seminar** (o dată la două săptămâni).

## Principiul

Studenții (viitori analiști, consultanți, consultanți de implementare) nu învață să scrie cod, ci să **gândească problema**: ce întrebare punem, ce metodă se potrivește, ce cerem asistentului AI, cum verificăm rezultatul și ce îi spunem clientului. Codul îl scrie asistentul.

## Cele șase elemente ale unui modul

| # | Element | Unde stă | Întrebarea la care răspunde |
|---|---|---|---|
| 1 | **Problema de business** | începutul `README.md` al modulului | Ce vrea clientul și ce decizie trebuie luată? |
| 2 | **Rolul studentului și livrabilul** | sub problemă, în `README.md` | Ce face studentul și ce predă la final? |
| 3 | **Conceptele** (cursul) | `curs-NN-*.ipynb` / `.pdf` | Ce metode se potrivesc și de ce? Cod scurt, doar ca ilustrație. |
| 4 | **Puntea curs → seminar** | finalul ultimului notebook de curs, începutul seminarului și `README.md` | 3-5 concepte cheie, o cerere-model către AI, lista de verificare |
| 5 | **Seminarul** | `seminar-NN-*.ipynb` | Studenții formulează cererile, rulează, verifică, interpretează |
| 6 | **Tema / proiectul** | `tema-NN-*.ipynb`, `07-proiect` | Același concept, pe alte date, cu **Jurnalul AI** completat |

## Problema de business: cum o scriem

- un **client concret** (manager de retenție, agenție imobiliară, director HR), cu cuvintele lui, între ghilimele;
- o **decizie** care depinde de răspuns („câți clienți contactăm?”), nu doar o curiozitate;
- un **set de date** din catalog (`incarca("lab-setN")`), ca exemplele să ruleze oriunde;
- când se poate, **cifre de business** (costuri, câștiguri) care fac legătura cu metrica (vezi `curs-06-evaluare-optimizare`).

## Notebook-ul de curs

1. antetul cursului, badge-ul Colab și celula „Configurare curs” (copiate dintr-un notebook existent din același modul);
2. „Problema de azi”: clientul și întrebările cursului;
3. câte o secțiune pe concept: **explicație scurtă → cel mult o celulă de cod → interpretare**;
4. o secțiune „Ce îi spunem clientului”: un rezumat cu cifre calculate în notebook;
5. puntea curs → seminar și link-ul către seminar.

Notebook-ul trebuie să ruleze complet în mai puțin de un minut (`Restart and run all`). Calculele lungi merg în `extra-*`.

## Seminarul (2 ore)

| Timp | Activitate |
|---|---|
| 20 min | demonstrație ghidată: cererea-model din punte, rulată și verificată împreună |
| 60 min | 3 exerciții: studenții scriu cererile, rulează, bifează verificările, răspund la întrebarea de interpretare |
| 30 min | același concept pe setul de date al proiectului |
| 10 min | discuție: ce a greșit asistentul și cum ne-am dat seama |

## Lista de verificare pentru un modul nou

- [ ] problema de business, rolul și livrabilul sunt în `README.md`;
- [ ] puntea curs → seminar este identică în curs, seminar și `README.md`;
- [ ] notebook-urile încarcă datele doar cu `incarca(...)` sau din `./date/` (fără căi locale);
- [ ] toate notebook-urile rulează de la zero, în Colab și în mediul local (`requirements-local.txt`);
- [ ] titlul din antet are numărul modulului (`Curs 6`, `Seminar 6`, `Tema 6`);
- [ ] `python tools/genereaza_readme.py` a actualizat tabelul din `README.md`.

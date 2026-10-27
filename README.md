<img src="imagini/unitbv_mie.png" width="90" align="left">

# SEED1: Știința Explorării și Exploatării Datelor

**Universitatea Transilvania din Brașov · SIIPA, Semestrul I · 2026-2027**<br>
Instructor: Conf. dr. Teodor Ștefan Bîldea · teodor.bildea@unitbv.ro

<br clear="left">

Cursul te învață **conceptele** explorării datelor și ale învățării automate (analiza exploratorie, vizualizare, reducerea dimensiunilor, clusterizare, regresie, clasificare) și cum să le aplici **lucrând cu un asistent AI**: descrii în limbaj natural ce vrei să obții, asistentul scrie codul, iar tu verifici și interpretezi rezultatele. Nu ai nevoie de experiență anterioară în programare.

- [Prezentarea generală a cursului](docs/prezentare-generala.md) (reguli, evaluare)
- [Ghid: cum lucrezi cu un asistent AI](docs/ghid-programare-asistata-ai.md)
- [Ghid: notebook-urile în Google Colab](docs/ghid-colab.md) (în browser, fără instalare)
- [Ghid: lucrul local, pe calculatorul tău](docs/ghid-local.md) (funcționează și fără internet)
- [Seturile de date ale cursului](docs/seturi-de-date.md)
- [Examen](examen/)

## Programa

Primele trei module (restul sunt în lucru), câte unul la două săptămâni: **2 ore de curs** (conceptele) și **2 ore de seminar** (aplicarea lor cu un asistent AI). Fiecare curs se încheie cu o „punte” (conceptele cheie, ce ceri asistentului, ce verifici), iar seminarul pornește exact de acolo. Materialele din anii anteriori, cu cod complet, sunt păstrate ca `extra` în pagina fiecărui modul.

Apasă **Open in Colab** ca să deschizi un notebook direct în browser, fără să instalezi nimic.

<!-- PROGRAMA -->
| Modul | Curs (2h) | Seminar (2h) | Temă |
|---|---|---|---|
| **1.** [Date, întrebări și lucrul cu AI](cursuri/01-date-intrebari-ai) | [Introducere](cursuri/01-date-intrebari-ai/curs-01-introducere.pdf) (PDF)<br>[![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sbildea/SEED/blob/main/cursuri/01-date-intrebari-ai/curs-01b-prompting-1-principii-si-tactici.ipynb) [Prompting 1 principii si tactici](cursuri/01-date-intrebari-ai/curs-01b-prompting-1-principii-si-tactici.ipynb)<br>[![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sbildea/SEED/blob/main/cursuri/01-date-intrebari-ai/curs-01b-prompting-2-iterare.ipynb) [Prompting 2 iterare](cursuri/01-date-intrebari-ai/curs-01b-prompting-2-iterare.ipynb)<br>[![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sbildea/SEED/blob/main/cursuri/01-date-intrebari-ai/curs-01b-prompting-3-rezumare.ipynb) [Prompting 3 rezumare](cursuri/01-date-intrebari-ai/curs-01b-prompting-3-rezumare.ipynb)<br>[![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sbildea/SEED/blob/main/cursuri/01-date-intrebari-ai/curs-01b-prompting-4-inferare.ipynb) [Prompting 4 inferare](cursuri/01-date-intrebari-ai/curs-01b-prompting-4-inferare.ipynb)<br>[![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sbildea/SEED/blob/main/cursuri/01-date-intrebari-ai/curs-01b-prompting-5-transformare.ipynb) [Prompting 5 transformare](cursuri/01-date-intrebari-ai/curs-01b-prompting-5-transformare.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sbildea/SEED/blob/main/cursuri/01-date-intrebari-ai/seminar-01-primul-notebook-cu-ai.ipynb) [Primul notebook cu ai](cursuri/01-date-intrebari-ai/seminar-01-primul-notebook-cu-ai.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sbildea/SEED/blob/main/cursuri/01-date-intrebari-ai/tema-01-exercitii-python.ipynb) [Exercitii python](cursuri/01-date-intrebari-ai/tema-01-exercitii-python.ipynb) |
| **2.** [Analiza exploratorie și vizualizarea datelor](cursuri/02-explorare-vizualizare) | [Analiza exploratorie](cursuri/02-explorare-vizualizare/curs-02-analiza-exploratorie.pdf) (PDF)<br>[Vizualizarea datelor](cursuri/02-explorare-vizualizare/curs-02-vizualizarea-datelor.pdf) (PDF)<br>[![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sbildea/SEED/blob/main/cursuri/02-explorare-vizualizare/curs-02-vizualizarea-datelor.ipynb) [Vizualizarea datelor](cursuri/02-explorare-vizualizare/curs-02-vizualizarea-datelor.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sbildea/SEED/blob/main/cursuri/02-explorare-vizualizare/seminar-02a-dataframe.ipynb) [Dataframe](cursuri/02-explorare-vizualizare/seminar-02a-dataframe.ipynb)<br>[![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sbildea/SEED/blob/main/cursuri/02-explorare-vizualizare/seminar-02b-vizualizarea-datelor.ipynb) [Vizualizarea datelor](cursuri/02-explorare-vizualizare/seminar-02b-vizualizarea-datelor.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sbildea/SEED/blob/main/cursuri/02-explorare-vizualizare/tema-02a-dataframe-analiza-exploratorie.ipynb) [Dataframe analiza exploratorie](cursuri/02-explorare-vizualizare/tema-02a-dataframe-analiza-exploratorie.ipynb)<br>[![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sbildea/SEED/blob/main/cursuri/02-explorare-vizualizare/tema-02b-vizualizarea-datelor.ipynb) [Vizualizarea datelor](cursuri/02-explorare-vizualizare/tema-02b-vizualizarea-datelor.ipynb) |
| **3.** [Învățare nesupervizată: PCA, clusterizare, asociere](cursuri/03-invatare-nesupervizata) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sbildea/SEED/blob/main/cursuri/03-invatare-nesupervizata/curs-03a-pca-clusterizare.ipynb) [Pca clusterizare](cursuri/03-invatare-nesupervizata/curs-03a-pca-clusterizare.ipynb)<br>[![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sbildea/SEED/blob/main/cursuri/03-invatare-nesupervizata/curs-03b-asociere-recomandari.ipynb) [Asociere recomandari](cursuri/03-invatare-nesupervizata/curs-03b-asociere-recomandari.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sbildea/SEED/blob/main/cursuri/03-invatare-nesupervizata/seminar-03-invatare-nesupervizata.ipynb) [Invatare nesupervizata](cursuri/03-invatare-nesupervizata/seminar-03-invatare-nesupervizata.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sbildea/SEED/blob/main/cursuri/03-invatare-nesupervizata/tema-03-invatare-nesupervizata.ipynb) [Invatare nesupervizata](cursuri/03-invatare-nesupervizata/tema-03-invatare-nesupervizata.ipynb) |
<!-- /PROGRAMA -->

## Pe scurt: cum folosești materialele

Ai două variante, cu aceleași notebook-uri:

- **În browser, cu Google Colab:** nu instalezi nimic, dar ai nevoie de internet. Pașii sunt mai jos.
- **Local, pe calculatorul tău:** instalezi Python o dată, apoi totul merge și fără internet. Vezi [ghidul local](docs/ghid-local.md).

În Colab:

1. Apasă **Open in Colab** lângă notebook și salvează o copie: **File → Save a copy in Drive**.
2. Rulează prima celulă, **Configurare curs**. Ea descarcă materialele și instalează pachetele (cam un minut). Dacă Colab avertizează că notebook-ul nu este creat de Google, apasă **Run anyway**.
3. Datele se încarcă cu o singură linie:

   ```python
   from seed.date import incarca
   date = incarca("lab-set4")   # toate tabelele setului
   df = date[0]                 # primul tabel
   ```

Detalii și probleme frecvente: [ghidul Colab](docs/ghid-colab.md) · [ghidul local](docs/ghid-local.md).

## Pentru profesor

- Instrucțiunile de publicare și actualizare anuală sunt în [docs/ghid-profesor.md](docs/ghid-profesor.md).
- Tabelul cu programa se regenerează cu `python tools/genereaza_readme.py`.

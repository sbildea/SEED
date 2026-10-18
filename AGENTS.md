# Instrucțiuni pentru asistenți AI care lucrează în acest repository

Cursul SEED1 (Știința Explorării și Exploatării Datelor), Universitatea Transilvania din Brașov. Materialele sunt în limba română; utilizatorii sunt studenți fără experiență de programare.

- Notebook-urile sunt în `cursuri/<NN-modul>/` (7 module: curs, seminar, temă, extra) și rulează din folderul lor (în Colab, prima celulă „Configurare curs" clonează repository-ul și face `cd` în acel folder).
- Seturile mari de date se încarcă **doar** cu `from seed.date import incarca`; `incarca("lab-set4")` întoarce un dicționar nume_tabel → DataFrame, accesibil și după poziție (`[0]`). Lista: `lista_seturi()` sau `docs/seturi-de-date.md`. Nu scrie căi absolute și nu descărca date de pe internet.
- Datele mici ale unei săptămâni sunt în `./date/` lângă notebook.
- Folosește pandas, matplotlib/seaborn, scikit-learn. Cod scurt, comentarii în română, explicații pas cu pas.
- La modelare: împarte train/test înainte de orice transformare învățată din date (fără data leakage) și folosește `random_state` cerut în enunț.
- În teme, nu rezolva exercițiul în locul studentului fără să explici conceptul; ajută-l să verifice rezultatele.

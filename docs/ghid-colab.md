# Ghid: notebook-urile cursului în Google Colab

Toate materialele cursului sunt într-un singur loc și nu trebuie să instalezi nimic: ai nevoie doar de un browser și de un cont Google.

## Unde găsești materialele

- **Slide-uri și documente:** deschide PDF-ul din folderul fiecărei săptămâni (tabelul din [README](../README.md)) sau descarcă totul deodată din **Releases → 2026-2027**.
- **Notebook-uri:** apasă butonul **Open in Colab** de lângă fiecare notebook din tabelul cu programa.

## Cum rulezi un notebook în Colab

1. Apasă **Open in Colab** și autentifică-te cu contul Google.
2. Apasă imediat **File → Save a copy in Drive**. De acum lucrezi pe copia ta. Versiunea cursului este doar pentru citire, așa că altfel modificările tale s-ar pierde.
3. Rulează prima celulă, **Configurare curs**. Ea descarcă fișierele cursului și instalează pachetele necesare în aproximativ un minut. Dacă Colab avertizează că notebook-ul nu este creat de Google, apasă **Run anyway**.
4. Rulează celelalte celule în ordine cu **Shift + Enter**.
5. Dacă ai nevoie de GPU: **Runtime → Change runtime type → T4 GPU** (doar când notebook-ul cere asta; timpul gratuit pe GPU este limitat).

## Datele

Seturile de date nu se mai descarcă manual. După celula de configurare:

```python
from seed.date import incarca, lista_seturi
lista_seturi()                  # ce seturi există
date = incarca("lab-set5")      # toate tabelele setului 5
date                            # arată tabelele și dimensiunile lor
df = date["credit_train"]       # un tabel după nume
df = date[1]                    # sau după poziție
```

Prima încărcare a unui set durează câteva secunde (se descarcă); apoi este instantanee până la resetarea sesiunii. Lista completă este în [seturi-de-date.md](seturi-de-date.md).

## Bine de știut

- Sesiunile Colab se resetează după o perioadă de inactivitate (aproximativ 90 de minute) sau după circa 12 ore. Copia salvată rămâne în Drive, dar trebuie să **rulezi din nou celula de configurare** la fiecare sesiune nouă.
- Fișierele create într-o sesiune (rezultate, grafice salvate) dispar la resetare. Ca să le păstrezi, salvează-le în Drive:

  ```python
  from google.colab import drive
  drive.mount('/content/drive')
  ```

- Ca să obții un notebook actualizat după ce profesorul a corectat ceva, deschide-l din nou de pe pagina cursului și salvează o copie nouă.
- Ai găsit o greșeală? Raporteaz-o în secțiunea **Issues** a repository-ului (necesită un cont GitHub gratuit) sau anunță profesorul.

## Probleme frecvente

| Problemă | Soluție |
| --- | --- |
| `ModuleNotFoundError: No module named 'seed'` | Nu ai rulat celula **Configurare curs** în sesiunea curentă. Rulează-o și apoi reia. |
| `ModuleNotFoundError` pentru alt pachet | Rulează din nou celula de configurare; dacă persistă, anunță profesorul. |
| Conflict de versiuni după configurare | **Runtime → Restart session**, apoi rulează din nou toate celulele. |
| Vezi o versiune veche a notebook-ului | Lucrezi pe copia ta salvată. Deschide-l din nou de pe pagina cursului. |

## Internet instabil?

Colab are nevoie de internet tot timpul. Dacă în laborator conexiunea este instabilă, lucrează local, pe calculatorul tău: [ghidul pentru lucrul local](ghid-local.md) arată cum pregătești totul acasă ca să funcționeze apoi fără internet.

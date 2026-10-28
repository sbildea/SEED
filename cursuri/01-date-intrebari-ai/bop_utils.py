"""Funcții ajutătoare pentru notebook-urile de prompting (curs-01b-prompting-*).

Folosește un model Gemini mic (Flash-Lite, cu limite gratuite largi) prin cheia API
personală a fiecărui student (gratuită):
  1. Intră pe https://aistudio.google.com/apikey cu contul Google și apasă „Create API key”.
  2. În Colab: iconița cu cheie (Secrets) din bara din stânga -> „Add new secret”,
     nume GOOGLE_API_KEY, valoare = cheia; activează „Notebook access”.
     Local: lipește cheia când ți se cere; poți alege s-o salvezi pe calculator (fișier în folderul
     tău de utilizator, în afara repository-ului), ca să nu o mai ceri data viitoare.
     Alternativ: variabila de mediu GOOGLE_API_KEY (numele exact, la singular), apoi repornește Jupyter/VS Code.
Nu scrie cheia în notebook și nu o urca pe GitHub.
"""

import getpass
import logging
import os
import sys
import time
from pathlib import Path

from google import genai

# Modelul folosit: alias către cel mai nou Flash-Lite (rapid, limite gratuite largi).
# Se poate schimba fără a modifica fișierul: os.environ["SEED_GEMINI_MODEL"] = "..."
MODEL = os.environ.get("SEED_GEMINI_MODEL", "gemini-flash-lite-latest")

# Ascunde avertismentul SDK-ului despre apelarea automată de funcții (AFC); nu afectează rezultatul.
logging.getLogger("google_genai.models").setLevel(logging.ERROR)


# Fișierul unde se poate salva cheia local (în folderul de utilizator, nu în repository).
FISIER_CHEIE = Path.home() / ".seed" / "gemini_api_key.txt"


def _in_colab():
    return "google.colab" in sys.modules


def sterge_cheia():
    """Șterge cheia salvată pe acest calculator (util pe calculatoare folosite în comun)."""
    FISIER_CHEIE.unlink(missing_ok=True)
    os.environ.pop("GOOGLE_API_KEY", None)
    print("Cheia salvată a fost ștearsă.")


def _salveaza_cheia(cheie):
    try:
        FISIER_CHEIE.parent.mkdir(parents=True, exist_ok=True)
        FISIER_CHEIE.write_text(cheie, encoding="utf-8")
        try:
            FISIER_CHEIE.chmod(0o600)  # doar utilizatorul curent (pe Windows nu are efect)
        except OSError:
            pass
        print(f"Cheia a fost salvată în {FISIER_CHEIE}. Pentru a o șterge: bop_utils.sterge_cheia()")
    except OSError as e:
        print("Nu am putut salva cheia:", e)


def _cheie_api():
    # variabila de mediu (numele GOOGLE_API_KEY sau GEMINI_API_KEY, ambele recunoscute de SDK)
    for nume in ("GOOGLE_API_KEY", "GEMINI_API_KEY"):
        if os.environ.get(nume, "").strip():
            return os.environ[nume].strip()
    try:  # Colab Secrets
        from google.colab import userdata
        cheie = userdata.get("GOOGLE_API_KEY")
        if cheie:
            return cheie
    except Exception:
        pass
    try:  # cheia salvată anterior pe acest calculator
        if FISIER_CHEIE.exists():
            cheie = FISIER_CHEIE.read_text(encoding="utf-8").strip()
            if cheie:
                return cheie
    except OSError:
        pass
    # nu am găsit cheia: explicăm de ce, apoi o cerem o singură dată
    print("Nu am găsit cheia API Gemini în variabila de mediu GOOGLE_API_KEY (și nici în Colab Secrets).")
    ghicite = [n for n in os.environ if n.upper().startswith(("GOOGLE_API_KEY", "GEMINI_API_KEY")) and n not in ("GOOGLE_API_KEY", "GEMINI_API_KEY")]
    if ghicite:
        print(f"Ai setat '{ghicite[0]}', dar numele corect este GOOGLE_API_KEY (singular, exact așa).")
    print("Dacă tocmai ai setat variabila, repornește Jupyter/VS Code ca să o vadă.")
    print("Sau lipește cheia acum. Cheie nouă: https://aistudio.google.com/apikey")
    cheie = getpass.getpass("Cheia API Gemini: ").strip()
    if not cheie:
        raise RuntimeError("Lipsește cheia API Gemini. Vezi instrucțiunile din bop_utils.py.")
    os.environ["GOOGLE_API_KEY"] = cheie  # vizibilă imediat, fără repornirea kernelului
    if not _in_colab():  # în Colab cheia se ține în Secrets; aici oferim salvarea locală
        print("Pe un calculator personal poți salva cheia, ca să nu o mai ceri data viitoare.")
        print("NU o salva pe un calculator folosit în comun (laborator, sală de calculatoare).")
        if input("Salvez cheia pe acest calculator? (d/n): ").strip().lower() in ("d", "da", "y", "yes"):
            _salveaza_cheia(cheie)
    return cheie


_client = None


def _gemini():
    global _client
    if _client is None:
        _client = genai.Client(api_key=_cheie_api())
    return _client


def get_news_sentiment(news_text: str) -> str:
    """
    Analyzes the sentiment of a given news article.
    Analizeaza sentimentul unei stiri date pentru a indeplini o sarcina legata de sentimentul unei stiri.
    """
    return "negativ"  # unealtă demonstrativă (tool calling), folosită în bop1


def get_completion(prompt=None, model=None):
    """Trimite promptul la Gemini și întoarce textul răspunsului."""
    if not prompt:
        return "no prompt provided"
    tic = time.time()
    try:
        response = _gemini().models.generate_content(
            model=model or MODEL,
            contents=[prompt],
            config={"tools": [get_news_sentiment]},
        )
    except Exception as e:
        mesaj = str(e)
        if "429" in mesaj or "RESOURCE_EXHAUSTED" in mesaj:
            return ("Ai atins limita gratuită de cereri (pe minut sau pe zi). "
                    "Așteaptă un minut și rulează din nou celula; dacă persistă, continuă mâine.")
        if "API key" in mesaj or "API_KEY" in mesaj or "403" in mesaj or "400" in mesaj:
            return "Cheia API pare greșită sau expirată. Creează alta pe https://aistudio.google.com/apikey"
        raise
    print("duration: ", round(time.time() - tic, 2))
    try:
        return response.text
    except Exception:
        return None

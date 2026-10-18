"""Funcții ajutătoare pentru notebook-urile de prompting (curs-01b-prompting-*).

Folosește modelul Gemini prin cheia API personală a fiecărui student (gratuită):
  1. Intră pe https://aistudio.google.com/apikey cu contul Google și apasă „Create API key”.
  2. În Colab: iconița cu cheie (Secrets) din bara din stânga -> „Add new secret”,
     nume GOOGLE_API_KEY, valoare = cheia; activează „Notebook access”.
     Local: setează variabila de mediu GOOGLE_API_KEY (sau introdu cheia când ți se cere).
Nu scrie cheia în notebook și nu o urca pe GitHub.
"""

import getpass
import os
import time

from google import genai

# Modelul folosit; se poate schimba fără a modifica fișierul: os.environ["SEED_GEMINI_MODEL"] = "..."
MODEL = os.environ.get("SEED_GEMINI_MODEL", "gemini-3-flash-preview")


def _cheie_api():
    if os.environ.get("GOOGLE_API_KEY"):
        return os.environ["GOOGLE_API_KEY"]
    try:  # Colab Secrets
        from google.colab import userdata
        cheie = userdata.get("GOOGLE_API_KEY")
        if cheie:
            return cheie
    except Exception:
        pass
    cheie = getpass.getpass("Cheia API Gemini (GOOGLE_API_KEY): ").strip()
    if not cheie:
        raise RuntimeError("Lipsește cheia API Gemini. Vezi instrucțiunile din bop_utils.py.")
    os.environ["GOOGLE_API_KEY"] = cheie
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
    response = _gemini().models.generate_content(
        model=model or MODEL,
        contents=[prompt],
        config={"tools": [get_news_sentiment]},
    )
    print("duration: ", round(time.time() - tic, 2))
    try:
        return response.text
    except Exception:
        return None

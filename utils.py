import os, json
from cryptography.fernet import Fernet
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from datetime import datetime

_KEYFILE = "secret.key"

def load_create_key(path = _KEYFILE):
    if os.path.exists(path):
        with open(path, "rb") as f:
            return f.read()
    key = Fernet.generate_key()
    with open(path, "rb") as f:
        f.write(key)
    return key


import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "database" / "gestion_commerciale.db"


def obtenir_connexion():
    connexion = sqlite3.connect(DB_PATH)
    connexion.execute("PRAGMA foreign_keys = ON")
    return connexion




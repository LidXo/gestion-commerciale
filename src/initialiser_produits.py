
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DB_PATH = BASE_DIR / "database" / "gestion_commerciale.db"
INSERT_PATH = BASE_DIR / "sql" / "insert_products.sql"

connexion = sqlite3.connect(DB_PATH)

try:
    connexion.execute("PRAGMA foreign_keys = ON")

    with open(INSERT_PATH, "r", encoding="utf-8") as fichier:
        script = fichier.read()

    connexion.executescript(script)

    print("Produits insérés avec succès.")

except sqlite3.Error as erreur:
    print("Erreur SQLite :", erreur)

finally:
    connexion.close()




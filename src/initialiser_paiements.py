
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DB_PATH = BASE_DIR / "database" / "gestion_commerciale.db"
PAYMENTS_PATH = BASE_DIR / "sql" / "insert_payments.sql"

connexion = sqlite3.connect(DB_PATH)

try:
    connexion.execute("PRAGMA foreign_keys = ON")

    with open(PAYMENTS_PATH, "r", encoding="utf-8") as fichier:
        script = fichier.read()

    connexion.executescript(
        "BEGIN;\n" + script + "\nCOMMIT;"
    )

    print("Paiements insérés avec succès.")

except (sqlite3.Error, OSError) as erreur:
    if connexion.in_transaction:
        connexion.rollback()

    print("Erreur :", erreur)

finally:
    connexion.close()




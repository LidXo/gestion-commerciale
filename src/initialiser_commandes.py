
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DB_PATH = BASE_DIR / "database" / "gestion_commerciale.db"

ORDERS_PATH = BASE_DIR / "sql" / "insert_orders.sql"
DETAILS_PATH = BASE_DIR / "sql" / "insert_order_details.sql"

connexion = sqlite3.connect(DB_PATH)

try:
    # Activer les clés étrangères
    connexion.execute("PRAGMA foreign_keys = ON")

    # Lire les deux fichiers SQL
    with open(ORDERS_PATH, "r", encoding="utf-8") as fichier:
        script_commandes = fichier.read()

    with open(DETAILS_PATH, "r", encoding="utf-8") as fichier:
        script_details = fichier.read()

    # Exécuter les deux scripts dans une transaction
    connexion.executescript(
        "BEGIN;\n"
        + script_commandes
        + "\n"
        + script_details
        + "\nCOMMIT;"
    )

    print("Commandes et détails insérés avec succès.")

except (sqlite3.Error, OSError) as erreur:
    if connexion.in_transaction:
        connexion.rollback()

    print("Erreur :", erreur)

finally:
    connexion.close()




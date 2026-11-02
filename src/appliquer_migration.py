
import sqlite3
from pathlib import Path

# Définition des chemins
BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "database" / "gestion_commerciale.db"
BACKUP_PATH = BASE_DIR / "database" / "gestion_commerciale_backup_avant_v2.db"
MIGRATION_PATH = BASE_DIR / "sql" / "migration_v2.sql"


def appliquer_migration():
    if not DB_PATH.exists():
        print("Erreur : base de données introuvable.")
        return

    if not MIGRATION_PATH.exists():
        print("Erreur : fichier de migration introuvable.")
        return

    connexion = sqlite3.connect(DB_PATH)

    try:
        # 1. Créer une sauvegarde de la base
        sauvegarde = sqlite3.connect(BACKUP_PATH)
        connexion.backup(sauvegarde)
        sauvegarde.close()

        print("Sauvegarde créée avec succès.")

        # 2. Lire le fichier SQL
        with open(MIGRATION_PATH, "r", encoding="utf-8") as fichier:
            script_sql = fichier.read()

        # 3. Exécuter la migration dans une transaction
        connexion.executescript(
            "BEGIN IMMEDIATE;\n"
            + script_sql
            + "\nCOMMIT;"
        )

        print("Migration V2 appliquée avec succès.")

    except sqlite3.Error as erreur:
        if connexion.in_transaction:
            connexion.rollback()

        print(f"Erreur SQL : {erreur}")
        print("La migration a été annulée.")

    finally:
        connexion.close()


if __name__ == "__main__":
    appliquer_migration()



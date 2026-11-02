
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "database" / "gestion_commerciale.db"

connexion = sqlite3.connect(DB_PATH)
connexion.execute("PRAGMA foreign_keys = ON")

try:
    # Vérifier les données existantes
    commandes = connexion.execute(
        "SELECT COUNT(*) FROM COMMANDE"
    ).fetchone()[0]

    paiements = connexion.execute(
        "SELECT COUNT(*) FROM PAIEMENT"
    ).fetchone()[0]

    print(f"Commandes enregistrées : {commandes}")
    print(f"Paiements enregistrés : {paiements}")

    # Tester un état de commande invalide
    try:
        connexion.execute("""
            INSERT INTO COMMANDE
                (id_commande, date_commande, etat, id_client)
            VALUES
                (999, '2026-11-02', 'INCONNU', 1)
        """)
        print("ERREUR : état invalide accepté.")
    except sqlite3.IntegrityError:
        print("OK : état de commande invalide refusé.")

    # Tester un mode de paiement invalide
    try:
        connexion.execute("""
            INSERT INTO PAIEMENT
                (id_paiement, montant, date_paiement, mode_paiement, id_commande)
            VALUES
                (999, 1000, '2026-11-02', 'CHEQUE_INCONNU', 1)
        """)
        print("ERREUR : mode de paiement invalide accepté.")
    except sqlite3.IntegrityError:
        print("OK : mode de paiement invalide refusé.")

finally:
    connexion.rollback()
    connexion.close()


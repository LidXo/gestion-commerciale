import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from database import obtenir_connexion


def test_connexion():
    connexion = obtenir_connexion()

    assert connexion is not None

    connexion.close()


def test_tables():
    connexion = obtenir_connexion()

    tables = connexion.execute("""
        SELECT name
        FROM sqlite_master
        WHERE type = 'table'
    """).fetchall()

    noms_tables = [table[0] for table in tables]

    tables_attendues = [
        "CLIENT",
        "FOURNISSEUR",
        "CATEGORIE",
        "PRODUIT",
        "COMMANDE",
        "DETAIL_COMMANDE",
        "PAIEMENT"
    ]

    for table in tables_attendues:
        assert table in noms_tables

    connexion.close()


def test_integrite_referentielle():
    connexion = obtenir_connexion()

    anomalies = connexion.execute(
        "PRAGMA foreign_key_check"
    ).fetchall()

    connexion.close()

    assert anomalies == []
    



def test_clients_enregistres():
    connexion = obtenir_connexion()

    nombre = connexion.execute(
        "SELECT COUNT(*) FROM CLIENT"
    ).fetchone()[0]

    connexion.close()

    assert nombre >= 3


def test_dix_produits_enregistres():
    connexion = obtenir_connexion()

    nombre = connexion.execute(
        "SELECT COUNT(*) FROM PRODUIT"
    ).fetchone()[0]

    connexion.close()

    assert nombre == 10


def test_montants_commandes():
    connexion = obtenir_connexion()

    resultats = connexion.execute("""
        SELECT
            id_commande,
            SUM(quantite * prix_unitaire)
        FROM DETAIL_COMMANDE
        GROUP BY id_commande
        ORDER BY id_commande
    """).fetchall()

    connexion.close()

    montants_attendus = [
        (1, 470000),
        (2, 232000),
        (3, 590000),
        (4, 95000)
    ]

    assert resultats == montants_attendus




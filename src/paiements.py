from database import obtenir_connexion


def afficher_paiements():
    connexion = obtenir_connexion()

    try:
        requete = """
            SELECT
                p.id_paiement,
                p.id_commande,
                cl.nom_client,
                p.montant,
                p.date_paiement,
                p.mode_paiement
            FROM PAIEMENT p
            JOIN COMMANDE c
                ON p.id_commande = c.id_commande
            JOIN CLIENT cl
                ON c.id_client = cl.id_client
            ORDER BY p.id_paiement;
        """

        paiements = connexion.execute(requete).fetchall()

        print("\n===== PAIEMENTS TECHSTORE =====")

        for paiement in paiements:
            print(paiement)

    finally:
        connexion.close()



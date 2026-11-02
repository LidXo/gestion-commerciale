from database import obtenir_connexion


def afficher_commandes():
    connexion = obtenir_connexion()

    try:
        requete = """
            SELECT
                c.id_commande,
                cl.nom_client,
                c.date_commande,
                c.etat,
                COALESCE(SUM(dc.quantite * dc.prix_unitaire), 0)
                    AS montant_total
            FROM COMMANDE c
            JOIN CLIENT cl
                ON c.id_client = cl.id_client
            LEFT JOIN DETAIL_COMMANDE dc
                ON c.id_commande = dc.id_commande
            GROUP BY
                c.id_commande,
                cl.nom_client,
                c.date_commande,
                c.etat
            ORDER BY c.id_commande;
        """

        commandes = connexion.execute(requete).fetchall()

        print("\n===== COMMANDES TECHSTORE =====")

        for commande in commandes:
            print(commande)

    finally:
        connexion.close()




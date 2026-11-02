from database import obtenir_connexion


def afficher_produits():
    connexion = obtenir_connexion()

    try:
        requete = """
            SELECT
                p.id_produit,
                p.nom_produit,
                p.prix,
                p.stock,
                c.nom_categorie
            FROM PRODUIT p
            JOIN CATEGORIE c
                ON p.id_categorie = c.id_categorie
            ORDER BY p.nom_produit;
        """

        produits = connexion.execute(requete).fetchall()

        print("\n===== CATALOGUE TECHSTORE =====")

        for produit in produits:
            print(produit)

    finally:
        connexion.close()





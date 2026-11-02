from paiements import afficher_paiements

afficher_paiements()

from commandes import afficher_commandes

afficher_commandes()


# from produits import afficher_produits

# afficher_produits()


# from clients import afficher_clients

# afficher_clients()



# from database import obtenir_connexion


# def afficher_clients():
#     connexion = obtenir_connexion()

#     try:
#         requete = """
#             SELECT id_client, nom_client, telephone, email, adresse
#             FROM CLIENT
#             ORDER BY id_client;
#         """

#         clients = connexion.execute(requete).fetchall()

#         for client in clients:
#             print(client)

#     finally:
#         connexion.close()


# afficher_clients()


# from database import obtenir_connexion


# def ajouter_client(nom, telephone, email, adresse):
#     connexion = obtenir_connexion()

#     try:
#         requete = """
#             INSERT INTO CLIENT
#                 (nom_client, telephone, email, adresse)
#             VALUES (?, ?, ?, ?)
#         """

#         connexion.execute(
#             requete,
#             (nom, telephone, email, adresse)
#         )

#         connexion.commit()
#         print("Client ajouté avec succès.")

#     except Exception as erreur:
#         connexion.rollback()
#         print(f"Erreur : {erreur}")

#     finally:
#         connexion.close()


# ajouter_client(
#     "Kodjo Agbeko",
#     "+22890000111",
#     "kodjo@gmail.com",
#     "Lomé"
# )


# from database import obtenir_connexion

# connexion = obtenir_connexion()

# try:
#     resultat = connexion.execute(
#         "SELECT COUNT(*) FROM CLIENT"
#     ).fetchone()

#     print("Connexion réussie à TechStore.")
#     print(f"Nombre de clients : {resultat[0]}")

# finally:
#     connexion.close()


# import sqlite3
# from pathlib import Path

# BASE_DIR = Path(__file__).resolve().parent.parent
# DB_PATH = BASE_DIR / "database" / "gestion_commerciale.db"

# connexion = sqlite3.connect(DB_PATH)

# try:
#     requete = """
#         SELECT
#             id_commande,
#             SUM(quantite * prix_unitaire) AS montant_total
#         FROM DETAIL_COMMANDE
#         GROUP BY id_commande;
#     """
    

#     resultats = connexion.execute(requete).fetchall()

#     print("===== MONTANT DES COMMANDES =====")

#     for ligne in resultats:
#         print(f"Commande {ligne[0]} : {ligne[1]:,} FCFA")

# finally:
#     connexion.close()



# import sqlite3
# from pathlib import Path

# BASE_DIR = Path(__file__).resolve().parent.parent
# DB_PATH = BASE_DIR / "database" / "gestion_commerciale.db"

# connexion = sqlite3.connect(DB_PATH)

# try:
#     connexion.execute("PRAGMA foreign_keys = ON")

#     tables = [
#         "CLIENT",
#         "FOURNISSEUR",
#         "CATEGORIE",
#         "PRODUIT",
#         "COMMANDE",
#         "DETAIL_COMMANDE",
#         "PAIEMENT"
#     ]

#     print("===== BILAN DE LA BASE TECHSTORE =====")

#     for table in tables:
#         resultat = connexion.execute(
#             f"SELECT COUNT(*) FROM {table}"
#         )
#         nombre = resultat.fetchone()[0]

#         print(f"{table:<20} : {nombre}")

#     # Vérification des clés étrangères
#     erreurs = connexion.execute(
#         "PRAGMA foreign_key_check"
#     ).fetchall()

#     print("\n===== INTEGRITE REFERENTIELLE =====")

#     if erreurs:
#         print("Anomalies détectées :", erreurs)
#     else:
#         print("Aucune anomalie détectée.")

# finally:
#     connexion.close()






# import sqlite3
# from pathlib import Path

# BASE_DIR = Path(__file__).resolve().parent.parent
# DB_PATH = BASE_DIR / "database" / "gestion_commerciale.db"

# connexion = sqlite3.connect(DB_PATH)

# try:
#     requete = """
#         SELECT
#             p.id_paiement,
#             p.montant,
#             p.date_paiement,
#             p.mode_paiement,
#             p.id_commande
#         FROM PAIEMENT p
#         ORDER BY p.id_commande, p.id_paiement;
#     """

#     paiements = connexion.execute(requete).fetchall()

#     for paiement in paiements:
#         print(paiement)

# finally:
#     connexion.close()




# import sqlite3
# from pathlib import Path

# BASE_DIR = Path(__file__).resolve().parent.parent
# DB_PATH = BASE_DIR / "database" / "gestion_commerciale.db"

# connexion = sqlite3.connect(DB_PATH)

# try:
#     requete = """
#         SELECT
#             c.id_commande,
#             c.date_commande,
#             c.etat,
#             cl.nom_client
#         FROM COMMANDE c
#         INNER JOIN CLIENT cl
#             ON c.id_client = cl.id_client
#         ORDER BY c.id_commande;
#     """

#     resultats = connexion.execute(requete).fetchall()

#     for ligne in resultats:
#         print(ligne)

# finally:
#     connexion.close()




# import sqlite3
# from pathlib import Path

# BASE_DIR = Path(__file__).resolve().parent.parent
# DB_PATH = BASE_DIR / "database" / "gestion_commerciale.db"

# connexion = sqlite3.connect(DB_PATH)

# try:
#     requete = """
#         SELECT
#             p.id_produit,
#             p.nom_produit,
#             p.prix,
#             p.stock,
#             c.nom_categorie,
#             f.nom
#         FROM PRODUIT p
#         INNER JOIN CATEGORIE c
#             ON p.id_categorie = c.id_categorie
#         INNER JOIN FOURNISSEUR f
#             ON p.id_fournisseur = f.id_fournisseur;
#     """

#     resultats = connexion.execute(requete).fetchall()

#     for ligne in resultats:
#         print(ligne)

# finally:
#     connexion.close()







# import sqlite3
# from pathlib import Path

# BASE_DIR = Path(__file__).resolve().parent.parent
# DB_PATH = BASE_DIR / "database" / "gestion_commerciale.db"

# connexion = sqlite3.connect(DB_PATH)

# try:
#     tables = [
#         "CLIENT",
#         "FOURNISSEUR",
#         "CATEGORIE",
#         "PRODUIT",
#         "COMMANDE",
#         "DETAIL_COMMANDE",
#         "PAIEMENT"
#     ]

#     for table in tables:
#         resultat = connexion.execute(
#             f"SELECT COUNT(*) FROM {table}"
#         )
#         nombre = resultat.fetchone()[0]

#         print(f"{table} : {nombre} enregistrement(s)")

# finally:
#     connexion.close()






# import sqlite3
# from pathlib import Path

# BASE_DIR = Path(__file__).resolve().parent.parent
# DB_PATH = BASE_DIR / "database" / "gestion_commerciale.db"

# connexion = sqlite3.connect(DB_PATH)

# try:
#     # Afficher les fournisseurs
#     print("=== FOURNISSEURS ===")

#     fournisseurs = connexion.execute(
#         "SELECT * FROM FOURNISSEUR"
#     )

#     for fournisseur in fournisseurs.fetchall():
#         print(fournisseur)

#     # Afficher les catégories
#     print("\n=== CATEGORIES ===")

#     categories = connexion.execute(
#         "SELECT * FROM CATEGORIE"
#     )

#     for categorie in categories.fetchall():
#         print(categorie)

# finally:
#     connexion.close()



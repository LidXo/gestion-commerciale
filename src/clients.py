from database import obtenir_connexion


def ajouter_client(nom, telephone, email, adresse):
    connexion = obtenir_connexion()

    try:
        requete = """
            INSERT INTO CLIENT
                (nom_client, telephone, email, adresse)
            VALUES (?, ?, ?, ?)
        """

        connexion.execute(
            requete,
            (nom, telephone, email, adresse)
        )

        connexion.commit()
        print("Client ajouté avec succès.")

    finally:
        connexion.close()


def afficher_clients():
    connexion = obtenir_connexion()

    try:
        requete = """
            SELECT id_client, nom_client, telephone, email, adresse
            FROM CLIENT
            ORDER BY id_client;
        """

        clients = connexion.execute(requete).fetchall()

        for client in clients:
            print(client)

    finally:
        connexion.close()
        



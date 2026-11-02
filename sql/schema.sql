CREATE TABLE IF NOT EXISTS CLIENT (
    id_client INTEGER PRIMARY KEY,
    nom_client TEXT NOT NULL,
    telephone TEXT,
    email TEXT UNIQUE,
    adresse TEXT
);


CREATE TABLE IF NOT EXISTS FOURNISSEUR (
    id_fournisseur INTEGER PRIMARY KEY,
    nom TEXT NOT NULL,
    telephone TEXT
);


CREATE TABLE IF NOT EXISTS CATEGORIE (
    id_categorie INTEGER PRIMARY KEY,
    nom_categorie TEXT NOT NULL
);


CREATE TABLE IF NOT EXISTS PRODUIT (
    id_produit INTEGER PRIMARY KEY,
    nom_produit TEXT NOT NULL,
    prix INTEGER NOT NULL CHECK (prix >= 0),
    stock INTEGER NOT NULL CHECK (stock >= 0),
    id_categorie INTEGER NOT NULL,
    id_fournisseur INTEGER NOT NULL,

    FOREIGN KEY (id_categorie)
        REFERENCES CATEGORIE(id_categorie),

    FOREIGN KEY (id_fournisseur)
        REFERENCES FOURNISSEUR(id_fournisseur)
);


CREATE TABLE IF NOT EXISTS COMMANDE (
    id_commande INTEGER PRIMARY KEY,
    date_commande TEXT NOT NULL
        CHECK (date(date_commande) IS NOT NULL),

    etat TEXT NOT NULL CHECK (
        etat IN ('LIVREE', 'VALIDEE', 'EN_COURS', 'ANNULEE')
    ),

    id_client INTEGER NOT NULL,

    FOREIGN KEY (id_client)
        REFERENCES CLIENT(id_client)
);


CREATE TABLE IF NOT EXISTS DETAIL_COMMANDE (
    id_commande INTEGER NOT NULL,
    id_produit INTEGER NOT NULL,
    quantite INTEGER NOT NULL CHECK (quantite > 0),
    prix_unitaire INTEGER NOT NULL CHECK (prix_unitaire >= 0),

    PRIMARY KEY (id_commande, id_produit),

    FOREIGN KEY (id_commande)
        REFERENCES COMMANDE(id_commande),

    FOREIGN KEY (id_produit)
        REFERENCES PRODUIT(id_produit)
);


CREATE TABLE IF NOT EXISTS PAIEMENT (
    id_paiement INTEGER PRIMARY KEY,

    montant INTEGER NOT NULL CHECK (montant > 0),

    date_paiement TEXT NOT NULL
        CHECK (date(date_paiement) IS NOT NULL),

    mode_paiement TEXT NOT NULL CHECK (
        mode_paiement IN ('ESPECES', 'FLOOZ', 'TMONEY', 'VIREMENT')
    ),

    id_commande INTEGER NOT NULL,

    FOREIGN KEY (id_commande)
        REFERENCES COMMANDE(id_commande)
);









# Modèle Relationnel — TechStore

## 1. Présentation

Le Modèle Logique de Données (MLD) traduit le modèle conceptuel en structures relationnelles.

Il définit les tables, leurs attributs, les clés primaires et les clés étrangères.

## 2. Schéma relationnel

### CLIENT
- id_client : INTEGER — PK
- nom_client : TEXT
- telephone : TEXT
- email : TEXT
- adresse : TEXT

### FOURNISSEUR
- id_fournisseur : INTEGER — PK
- nom : TEXT
- telephone : TEXT

### CATEGORIE
- id_categorie : INTEGER — PK
- nom_categorie : TEXT

### PRODUIT
- id_produit : INTEGER — PK
- nom_produit : TEXT
- prix : INTEGER
- stock : INTEGER
- id_categorie : INTEGER — FK
- id_fournisseur : INTEGER — FK

### COMMANDE
- id_commande : INTEGER — PK
- date_commande : TEXT
- etat : TEXT
- id_client : INTEGER — FK

### PAIEMENT
- id_paiement : INTEGER — PK
- montant : INTEGER
- date_paiement : TEXT
- mode_paiement : TEXT
- id_commande : INTEGER — FK

### DETAIL_COMMANDE
- id_commande : INTEGER — PK, FK
- id_produit : INTEGER — PK, FK
- quantite : INTEGER
- prix_unitaire : INTEGER

## 3. Clés primaires et étrangères

Une clé primaire (PK) identifie de manière unique chaque enregistrement d'une table.

Une clé étrangère (FK) établit une relation entre deux tables et permet de préserver l'intégrité référentielle.

| Table | Clé primaire | Clés étrangères |
|---|---|---|
| CLIENT | id_client | Aucune |
| FOURNISSEUR | id_fournisseur | Aucune |
| CATEGORIE | id_categorie | Aucune |
| PRODUIT | id_produit | id_categorie, id_fournisseur |
| COMMANDE | id_commande | id_client |
| PAIEMENT | id_paiement | id_commande |
| DETAIL_COMMANDE | id_commande, id_produit | id_commande, id_produit |

## 4. Justification de DETAIL_COMMANDE

La relation entre COMMANDE et PRODUIT est de type plusieurs-à-plusieurs.

Une commande peut contenir plusieurs produits et un produit peut apparaître dans plusieurs commandes.

La table DETAIL_COMMANDE résout cette relation.

Sa clé primaire composée est constituée de :
- id_commande
- id_produit

Elle contient également :
- quantite : nombre d'unités commandées
- prix_unitaire : prix appliqué au moment de la vente

Le prix_unitaire conserve l'historique du prix de vente, même si le prix actuel du produit change dans la table PRODUIT.

## 5. Choix techniques

### SGBD
SQLite a été choisi pour sa simplicité, sa gratuité et son fonctionnement local sans serveur.

### Types de données
- INTEGER : identifiants, prix, montants, stocks et quantités.
- TEXT : noms, adresses, téléphones, états et dates.

Les montants sont stockés en FCFA sous forme d'entiers afin d'éviter les imprécisions liées aux nombres à virgule flottante.

Les numéros de téléphone sont stockés en TEXT afin de conserver les préfixes internationaux et les zéros initiaux.

Les dates sont stockées au format ISO 8601 : YYYY-MM-DD.

## 6. Intégrité référentielle

Les clés étrangères empêchent notamment :
- d'affecter un produit à une catégorie inexistante ;
- d'associer une commande à un client inexistant ;
- d'enregistrer un paiement pour une commande inexistante.

Dans SQLite, l'application doit activer les clés étrangères sur chaque connexion :

```sql
PRAGMA foreign_keys = ON;
```

Cette activation est réalisée dans le module Python database.py.

## 7. Conclusion

Le modèle relationnel permet de structurer les informations commerciales dans sept tables liées entre elles. Il limite les incohérences et facilite les opérations de consultation et d'analyse avec SQL.
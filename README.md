# TechStore — Base de données de gestion commerciale

## 1. Présentation du projet

TechStore est un projet de conception et de développement d'une base de données relationnelle destinée à une entreprise fictive spécialisée dans la vente de matériel informatique, de téléphones et d'accessoires électroniques.

Le projet vise à centraliser les informations commerciales afin de faciliter la gestion des clients, des produits, des fournisseurs, des commandes et des paiements.

## 2. Objectifs

- Concevoir une base de données relationnelle cohérente.
- Mettre en œuvre les relations entre les différentes entités.
- Garantir l'intégrité des données.
- Maîtriser les opérations SQL essentielles.
- Exploiter les données commerciales avec des requêtes SQL.
- Connecter une base SQLite à une application Python.
- Mettre en place des tests automatisés.

## 3. Technologies utilisées

| Technologie | Utilisation |
|---|---|
| SQLite | Système de gestion de base de données |
| SQL | Création, manipulation et interrogation des données |
| Python | Interaction avec la base de données |
| sqlite3 | Connexion Python-SQLite |
| pytest | Tests automatisés |
| Git / GitHub | Gestion de versions et hébergement du projet |
| Visual Studio Code | Environnement de développement |

## 4. Architecture de la base de données

La base de données comprend sept tables :

1. CLIENT
2. FOURNISSEUR
3. CATEGORIE
4. PRODUIT
5. COMMANDE
6. DETAIL_COMMANDE
7. PAIEMENT

### Principales relations

- Un client peut passer plusieurs commandes.
- Une commande appartient à un seul client.
- Une commande peut contenir plusieurs produits.
- Un produit peut apparaître dans plusieurs commandes.
- Un fournisseur peut fournir plusieurs produits.
- Une catégorie peut regrouper plusieurs produits.
- Une commande peut recevoir plusieurs paiements.

## 5. Fonctionnalités réalisées

### Gestion des données
- Enregistrement des clients.
- Consultation des clients.
- Consultation du catalogue des produits.
- Consultation des commandes.
- Consultation des paiements.

### Exploitation SQL
- Calcul du montant de chaque commande.
- Calcul du chiffre d'affaires réalisé.
- Requêtes d'analyse commerciale.

### Intégration Python
- Connexion à SQLite.
- Exécution de requêtes SQL depuis Python.
- Organisation du code en modules.
- Utilisation de paramètres SQL pour les insertions.

### Tests
- Vérification de la connexion.
- Vérification de la présence des tables.
- Vérification de l'intégrité référentielle.
- Vérification des données enregistrées.
- Vérification des montants des commandes.

## 6. Structure du projet

```text
gestion-commerciale/
│
├── database/
│   └── gestion_commerciale.db
│
├── sql/
│   ├── schema.sql
│   ├── insert_data.sql
│   ├── insert_reference_data.sql
│   ├── insert_products.sql
│   ├── insert_orders.sql
│   ├── insert_order_details.sql
│   ├── insert_payments.sql
│   └── queries.sql
│
├── src/
│   ├── database.py
│   ├── main.py
│   ├── clients.py
│   ├── produits.py
│   ├── commandes.py
│   ├── paiements.py
│   ├── initialiser_donnees.py
│   ├── initialiser_produits.py
│   ├── initialiser_commandes.py
│   └── initialiser_paiements.py
│
├── tests/
│   └── test_database.py
│
├── docs/
│   ├── modele_conceptuel.md
│   ├── modele_relationnel.md
│   └── regles_gestion.md
│
├── README.md
└── .gitignore
```

## 7. Installation et exécution

### Prérequis

- Python 3.10 ou supérieur.
- SQLite (intégré au module Python `sqlite3`).
- Git (facultatif).

### Cloner le projet

```bash
git clone URL_DU_DEPOT
cd gestion-commerciale
```

### Installer pytest

```bash
python -m pip install pytest
```

### Exécuter l'application

```bash
python src/main.py
```

### Exécuter les tests

```bash
python -m pytest -v
```

## 8. Résultats des tests

Les tests automatisés couvrent :

- La connexion à la base de données.
- La présence des sept tables.
- L'intégrité référentielle.
- La présence des clients.
- La présence des dix produits.
- L'exactitude des montants des commandes.

## 9. Limites et améliorations futures

- Ajouter la modification et la suppression des clients.
- Développer une interface utilisateur.
- Automatiser la mise à jour des stocks.
- Renforcer le contrôle des paiements et des impayés.
- Développer un tableau de bord commercial.
- Ajouter des tests pour les opérations métier.

## 10. Auteur

**ABIYI Lidao**

Étudiant en Informatique — spécialité IA & Big Data

Projet pédagogique : Conception et développement d'une base de données de gestion commerciale.

---

*Projet réalisé dans un objectif d'apprentissage pratique de SQL, SQLite et Python.*



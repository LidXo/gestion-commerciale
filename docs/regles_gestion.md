# Règles de Gestion — TechStore

## 1. Présentation

Les règles de gestion définissent les contraintes métier applicables aux données et aux opérations commerciales de TechStore.

Elles servent de référence pour la conception de la base de données et le développement de l'application.

## 2. Gestion des clients

RG01 — Chaque client possède un identifiant unique.

RG02 — Un client peut passer plusieurs commandes.

RG03 — Une commande doit obligatoirement être associée à un client existant.

RG04 — Les coordonnées du client sont conservées dans la table CLIENT.

## 3. Gestion des fournisseurs

RG05 — Chaque fournisseur possède un identifiant unique.

RG06 — Un fournisseur peut fournir plusieurs produits.

RG07 — Dans la version actuelle, chaque produit est associé à un seul fournisseur.

## 4. Gestion des catégories et produits

RG08 — Chaque catégorie possède un identifiant unique.

RG09 — Une catégorie peut contenir plusieurs produits.

RG10 — Chaque produit appartient à une seule catégorie.

RG11 — Chaque produit possède un prix et une quantité en stock.

RG12 — Le prix enregistré dans PRODUIT représente le prix actuel du catalogue.

## 5. Gestion des commandes

RG13 — Chaque commande possède un identifiant unique.

RG14 — Une commande appartient à un seul client.

RG15 — Une commande doit contenir au moins un produit.

RG16 — Une commande peut contenir plusieurs produits.

RG17 — Un produit peut apparaître dans plusieurs commandes.

RG18 — La quantité commandée et le prix appliqué sont enregistrés dans DETAIL_COMMANDE.

RG19 — Le prix_unitaire conserve le prix appliqué lors de la commande.

RG20 — Les commandes peuvent avoir différents états : LIVREE, VALIDEE, EN_COURS ou ANNULEE.

RG21 — Une commande annulée ne doit pas être comptabilisée dans le chiffre d'affaires réalisé.

## 6. Gestion des paiements

RG22 — Un paiement est obligatoirement associé à une commande existante.

RG23 — Une commande peut ne recevoir aucun paiement ou recevoir plusieurs paiements.

RG24 — Chaque paiement possède un montant, une date et un mode de paiement.

RG25 — Une commande peut être réglée en plusieurs fois.

RG26 — Le montant total des paiements permet de déterminer la somme encaissée pour une commande.

## 7. Règles financières

RG27 — Les montants financiers sont exprimés en FCFA.

RG28 — Le montant total d'une commande est calculé ainsi :

Montant total = Somme (quantité × prix_unitaire).

RG29 — Le chiffre d'affaires réalisé correspond à la somme des montants des commandes livrées.

RG30 — Les encaissements correspondent à la somme des paiements enregistrés.

RG31 — Le chiffre d'affaires réalisé et les encaissements sont deux indicateurs distincts.

## 8. Règles techniques

RG32 — Chaque table possède une clé primaire.

RG33 — Les relations entre les tables sont assurées par des clés étrangères.

RG34 — Les clés étrangères doivent être activées dans chaque connexion SQLite.

RG35 — Les requêtes SQL exécutées depuis Python doivent utiliser des paramètres pour les données externes.

RG36 — Les opérations qui modifient plusieurs données liées doivent être exécutées dans une transaction lorsque nécessaire.

## 9. Limites actuelles

Certaines règles nécessitent encore un contrôle au niveau de l'application Python :

- Vérifier qu'une commande possède au moins une ligne de détail.
- Empêcher un stock négatif.
- Décrémenter le stock après une vente.
- Empêcher les paiements cumulés de dépasser le montant de la commande.
- Encadrer les valeurs autorisées pour les états et les modes de paiement.

Ces contrôles ne doivent pas être considérés comme automatiquement garantis par le schéma actuel.

## 10. Conclusion

Ces règles constituent le référentiel fonctionnel de TechStore. Elles permettent de vérifier la cohérence des données et de guider les évolutions futures du système.


## Contrôles d'intégrité ajoutés — Migration V2

La migration V2 ajoute quatre triggers SQLite :

- `verifier_commande_insert` : contrôle l'état et la date lors de l'insertion d'une commande.
- `verifier_commande_update` : contrôle l'état et la date lors de la modification d'une commande.
- `verifier_paiement_insert` : contrôle le mode et la date lors de l'insertion d'un paiement.
- `verifier_paiement_update` : contrôle le mode et la date lors de la modification d'un paiement.

États autorisés :
- LIVREE
- VALIDEE
- EN_COURS
- ANNULEE

Modes de paiement autorisés :
- ESPECES
- FLOOZ
- TMONEY
- VIREMENT

La migration a été exécutée et les tests d'insertion avec des états et modes de paiement invalides ont été réussis.

Limite : les tests de validation des dates et des opérations UPDATE restent à effectuer.


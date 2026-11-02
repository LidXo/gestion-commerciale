-- Afficher tous les clients
SELECT * 
FROM CLIENT;

-- Afficher uniqquement les noms et les adresses des clients
SELECT nom_client, adresse
FROM CLIENT;

-- EXO 1

SELECT
    id_commande,
    SUM(quantite * prix_unitaire) AS montant_total
FROM DETAIL_COMMANDE
GROUP BY id_commande;


-- EXERCICE 2 : Chiffre d'affaires réalisé

SELECT
    COALESCE(SUM(dc.quantite * dc.prix_unitaire), 0) AS chiffre_affaires
FROM COMMANDE c
JOIN DETAIL_COMMANDE dc
    ON dc.id_commande = c.id_commande
WHERE c.etat = 'LIVREE';






INSERT OR IGNORE INTO PAIEMENT
    (id_paiement, montant, date_paiement, mode_paiement, id_commande)
VALUES
    -- Commande 1 : paiement intégral
    (1, 470000, '2026-10-15', 'ESPECES', 1),

    -- Commande 2 : paiement partiel
    (2, 100000, '2026-10-18', 'FLOOZ', 2),

    -- Commande 3 : deux versements
    (3, 200000, '2026-10-20', 'TMONEY', 3),
    (4, 100000, '2026-10-21', 'FLOOZ', 3);




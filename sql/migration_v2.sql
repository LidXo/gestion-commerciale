
-- =====================================================
-- MIGRATION V2 : RENFORCEMENT DES REGLES DE GESTION
-- =====================================================

-- Vérification des commandes lors d'une insertion
CREATE TRIGGER IF NOT EXISTS verifier_commande_insert
BEFORE INSERT ON COMMANDE
FOR EACH ROW
WHEN
    NEW.etat NOT IN ('LIVREE', 'VALIDEE', 'EN_COURS', 'ANNULEE')
    OR date(NEW.date_commande) IS NULL
BEGIN
    SELECT RAISE(ABORT, 'Etat ou date de commande invalide');
END;

-- Vérification des commandes lors d'une modification
CREATE TRIGGER IF NOT EXISTS verifier_commande_update
BEFORE UPDATE OF etat, date_commande ON COMMANDE
FOR EACH ROW
WHEN
    NEW.etat NOT IN ('LIVREE', 'VALIDEE', 'EN_COURS', 'ANNULEE')
    OR date(NEW.date_commande) IS NULL
BEGIN
    SELECT RAISE(ABORT, 'Etat ou date de commande invalide');
END;

-- Vérification des paiements lors d'une insertion
CREATE TRIGGER IF NOT EXISTS verifier_paiement_insert
BEFORE INSERT ON PAIEMENT
FOR EACH ROW
WHEN
    NEW.mode_paiement NOT IN ('ESPECES', 'FLOOZ', 'TMONEY', 'VIREMENT')
    OR date(NEW.date_paiement) IS NULL
BEGIN
    SELECT RAISE(ABORT, 'Mode ou date de paiement invalide');
END;

-- Vérification des paiements lors d'une modification
CREATE TRIGGER IF NOT EXISTS verifier_paiement_update
BEFORE UPDATE OF mode_paiement, date_paiement ON PAIEMENT
FOR EACH ROW
WHEN
    NEW.mode_paiement NOT IN ('ESPECES', 'FLOOZ', 'TMONEY', 'VIREMENT')
    OR date(NEW.date_paiement) IS NULL
BEGIN
    SELECT RAISE(ABORT, 'Mode ou date de paiement invalide');
END;




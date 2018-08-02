from unittest.mock import Mock

from il_manque_du_beurre.application.produits_api import ProduitsAPI
from il_manque_du_beurre.domaine.produit_inconnu_exception import ProduitInconnuException
from il_manque_du_beurre.domaine.produit_manquant_service import ProduitManquantService

NOM_DE_PRODUIT_MANQUANT = 'beurre'
NOM_DE_PRODUIT_INCONNU = 'poivron bleu'


class TestProduitAPI:
    def setup_method(self):
        self.produit_manquant_service = Mock(ProduitManquantService)
        self.produits_api = ProduitsAPI(self.produit_manquant_service)

    def test_signale_qu_un_produit_est_manquant(self):
        resultat, status = self.produits_api.signaler_produit_manquant(NOM_DE_PRODUIT_MANQUANT)

        self.produit_manquant_service.signale.assert_called_with(NOM_DE_PRODUIT_MANQUANT)
        assert resultat == ''
        assert status == 201

    def test_renvoie_une_erreur_quand_un_produit_est_inconnu(self):
        self.produit_manquant_service.signale.side_effect = \
            ProduitInconnuException(NOM_DE_PRODUIT_INCONNU)

        resultat, status = self.produits_api.signaler_produit_manquant(NOM_DE_PRODUIT_INCONNU)

        assert resultat == 'Produit inconnu : "poivron bleu"'
        assert status == 400

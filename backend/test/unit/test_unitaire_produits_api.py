from unittest.mock import Mock

from il_manque_du_beurre.application.produits_api import ProduitsAPI
from il_manque_du_beurre.domaine.produit_manquant import ProduitManquant
from il_manque_du_beurre.domaine.produit_manquant_service import ProduitManquantService

NOM_DE_PRODUIT_MANQUANT = 'beurre'


class TestProduitAPI:
    def test_signale_qu_un_produit_est_manquant(self):
        produit = ProduitManquant.de_nom(NOM_DE_PRODUIT_MANQUANT)
        produit_manquant_service = Mock(ProduitManquantService)
        produits_api = ProduitsAPI(produit_manquant_service)

        produits_api.signaler_produit_manquant(NOM_DE_PRODUIT_MANQUANT)

        produit_manquant_service.signale.assert_called_with(produit)

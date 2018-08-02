from unittest.mock import Mock

from il_manque_du_beurre.domaine.produit_manquant import ProduitManquant
from il_manque_du_beurre.domaine.produit_manquant_repository import ProduitManquantRepository
from il_manque_du_beurre.domaine.produit_manquant_service import ProduitManquantService

NOM_DE_PRODUIT_MANQUANT = 'beurre'


class TestProduitManquantService:
    def test_signale_qu_un_produit_est_manquant(self):
        produit_manquant = ProduitManquant.de_nom(NOM_DE_PRODUIT_MANQUANT)
        produit_manquant_repository = Mock(ProduitManquantRepository)
        produit_manquant_service = ProduitManquantService(produit_manquant_repository)

        produit_manquant_service.signale(produit_manquant)

        produit_manquant_repository.ajoute.assert_called_with(produit_manquant)

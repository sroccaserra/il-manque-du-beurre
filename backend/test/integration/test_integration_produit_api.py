from unittest.mock import Mock

from il_manque_du_beurre.application.produits_api import ProduitAPI
from il_manque_du_beurre.domaine.produit_manquant_repository import ProduitManquantRepository
from il_manque_du_beurre.domaine.produit_manquant_service import ProduitManquantService


class TestProduitAPI:
    def test_signaler_un_produit_manquant_renvoie_201(self):
        nom_de_produit_manquant = 'beurre'
        produit_manquant_repository = Mock(ProduitManquantRepository)
        produit_manquant_service = ProduitManquantService(produit_manquant_repository)
        produit_api = ProduitAPI(produit_manquant_service)

        body, status = produit_api.signaler_produit_manquant(nom_de_produit_manquant)

        assert body == ''
        assert status == 201

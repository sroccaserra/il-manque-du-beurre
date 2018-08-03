import json

from il_manque_du_beurre.application.produits_api import ProduitsAPI
from il_manque_du_beurre.domaine.produit_manquant_repository import ProduitManquantRepository
from il_manque_du_beurre.domaine.produit_manquant_service import ProduitManquantService


class TestIntegrationProduitAPI:
    def test_signaler_un_produit_manquant_renvoie_200(self):
        nom_de_produit_manquant = 'beurre'
        produit_manquant_repository = ProduitManquantRepository()
        produit_manquant_service = ProduitManquantService(produit_manquant_repository)
        produits_api = ProduitsAPI(produit_manquant_service)

        response = produits_api.signaler_produit_manquant(nom_de_produit_manquant)

        assert response.data == b''
        assert response.status == '200 OK'
        assert response.mimetype == 'application/json'

    def test_lister_les_produits_manquants(self):
        nom_de_produit_manquant = 'beurre'
        produit_manquant_repository = ProduitManquantRepository()
        produit_manquant_service = ProduitManquantService(produit_manquant_repository)
        produits_api = ProduitsAPI(produit_manquant_service)
        produits_api.signaler_produit_manquant(nom_de_produit_manquant)

        response = produits_api.liste_des_produits_manquants()

        assert response.data == json_contenant([{'nom': 'beurre'}])
        assert response.status == '200 OK'
        assert response.mimetype == 'application/json'


def json_contenant(structure):
    return bytes(json.dumps(structure), encoding='utf-8')

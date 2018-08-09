import json

from il_manque_du_beurre.application.produits_api import ProduitsAPI
from il_manque_du_beurre.domaine.produit_manquant_service import ProduitManquantService
from il_manque_du_beurre.infrastructure.produit_manquant.produit_manquant_sql_repository import \
    ProduitManquantSqlRepository
from test.integration.database.database_test_base_class import DatabaseTestBaseClass

NOM_DE_PRODUIT_CONNU = 'beurre'


class TestIntegrationProduitAPI(DatabaseTestBaseClass):
    def setup_method(self):
        super().setup_method()
        produit_manquant_repository = ProduitManquantSqlRepository(self.data_store)
        produit_manquant_service = ProduitManquantService(produit_manquant_repository)
        self.produits_api = ProduitsAPI(produit_manquant_service)

    def test_signaler_un_produit_manquant_renvoie_200(self):

        response = self.produits_api.signaler_produit_manquant(NOM_DE_PRODUIT_CONNU)

        assert response.data == b''
        assert response.status == '200 OK'
        assert response.mimetype == 'application/json'

    def test_lister_les_produits_manquants(self):
        self.produits_api.signaler_produit_manquant(NOM_DE_PRODUIT_CONNU)

        response = self.produits_api.liste_des_produits_manquants()

        assert response.data == json_contenant([{'nom': NOM_DE_PRODUIT_CONNU}])
        assert response.status == '200 OK'
        assert response.mimetype == 'application/json'

    def test_signaler_qu_un_produit_n_est_plus_manquant(self):

        response = self.produits_api.signaler_produit_non_manquant(NOM_DE_PRODUIT_CONNU)

        assert response.data == b''
        assert response.status == '200 OK'
        assert response.mimetype == 'application/json'


def json_contenant(structure):
    return bytes(json.dumps(structure), encoding='utf-8')

from il_manque_du_beurre.infrastructure.produit_manquant.produit_manquant_sql_repository import \
    ProduitManquantSqlRepository
from test.integration.database.data_store_for_tests import data_store_for_tests


class TestProduitManquantSqlRepository:
    def xtest_liste_des_produits_manquants_vide(self):
        data_store = data_store_for_tests()
        produits_manquants_repository = ProduitManquantSqlRepository(data_store)

        produits_manquants = produits_manquants_repository.liste_des_produits_manquants()

        assert produits_manquants == []

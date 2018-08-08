from il_manque_du_beurre.domaine.produit_manquant import ProduitManquant
from il_manque_du_beurre.infrastructure.produit_manquant.produit_manquant_sql_repository import \
    ProduitManquantSqlRepository

from test.integration.database.database_test_base_class import DatabaseTestBaseClass

PRODUIT_MANQUANT = ProduitManquant('beurre')


class TestProduitManquantSqlRepository(DatabaseTestBaseClass):
    def test_liste_des_produits_manquants_vide(self):
        produits_manquants_repository = ProduitManquantSqlRepository(self.data_store)

        produits_manquants = produits_manquants_repository.liste_des_produits_manquants()

        assert produits_manquants == []

    def test_liste_des_produits_manquants_apres_avoir_signale_du_beurre(self):
        produits_manquants_repository = ProduitManquantSqlRepository(self.data_store)
        produits_manquants_repository.ajoute(PRODUIT_MANQUANT)

        produits_manquants = produits_manquants_repository.liste_des_produits_manquants()

        assert produits_manquants == [PRODUIT_MANQUANT]

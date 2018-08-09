from il_manque_du_beurre.domaine.produit_manquant import ProduitManquant
from il_manque_du_beurre.infrastructure.produit_manquant.produit_manquant_sql_repository import \
    ProduitManquantSqlRepository

from test.integration.database.database_test_base_class import DatabaseTestBaseClass

PRODUIT_MANQUANT = ProduitManquant('beurre')


class TestProduitManquantSqlRepository(DatabaseTestBaseClass):
    def setup_method(self):
        super().setup_method()
        self.repository = ProduitManquantSqlRepository(self.data_store)

    def test_liste_des_produits_manquants_vide(self):
        produits_manquants = self.repository.liste_des_produits_manquants()

        assert produits_manquants == []

    def test_liste_des_produits_manquants_apres_avoir_signale_du_beurre(self):
        self.repository.ajoute(PRODUIT_MANQUANT)

        produits_manquants = self.repository.liste_des_produits_manquants()

        assert produits_manquants == [PRODUIT_MANQUANT]

    def test_signaler_un_produit_manquant_deux_fois_est_possible(self):
        self.repository.ajoute(PRODUIT_MANQUANT)
        self.repository.ajoute(PRODUIT_MANQUANT)

        produits_manquants = self.repository.liste_des_produits_manquants()

        assert produits_manquants == [PRODUIT_MANQUANT]

    def test_le_beurre_est_un_produit_connu(self):
        assert self.repository.est_un_nom_de_produit_connu(PRODUIT_MANQUANT.nom)

from il_manque_du_beurre.domaine.produit_manquant import ProduitManquant
from il_manque_du_beurre.domaine.produit_manquant_repository import ProduitManquantRepository

NOM_DE_PRODUIT_CONNU = 'beurre'
NOM_DE_PRODUIT_INCONNU = 'poivron bleu'
PRODUIT_MANQUANT = ProduitManquant(NOM_DE_PRODUIT_CONNU)


class TestProduitManquantRepository:
    def setup_method(self):
        self.repository = ProduitManquantRepository()

    def test_le_beurre_est_un_produit_connu(self):
        assert self.repository.est_un_nom_de_produit_connu(NOM_DE_PRODUIT_CONNU)

    def test_le_poivron_bleu_est_un_produit_inconnu(self):
        assert not self.repository.est_un_nom_de_produit_connu(
            NOM_DE_PRODUIT_INCONNU)

    def test_lister_les_produits_manquants(self):
        self.repository.ajoute(PRODUIT_MANQUANT)
        assert [PRODUIT_MANQUANT] == self.repository.liste_des_produits_manquants()

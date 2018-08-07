from unittest.mock import Mock

import pytest

from il_manque_du_beurre.domaine.produit_inconnu_exception import ProduitInconnuException
from il_manque_du_beurre.domaine.produit_manquant import ProduitManquant
from il_manque_du_beurre.domaine.produit_manquant_repository import ProduitManquantRepository
from il_manque_du_beurre.domaine.produit_manquant_service import ProduitManquantService

NOM_DE_PRODUIT_MANQUANT = 'beurre'
NOM_DE_PRODUIT_INCONNU = 'poivron bleu'
PRODUIT_MANQUANT = ProduitManquant(NOM_DE_PRODUIT_MANQUANT)


class TestProduitManquantService:
    def setup_method(self):
        self.produit_manquant_repository = Mock(ProduitManquantRepository)
        self.produit_manquant_repository.est_un_nom_de_produit_connu.return_value = True
        self.produit_manquant_service = ProduitManquantService(self.produit_manquant_repository)

    def test_signale_qu_un_produit_est_manquant(self):
        produit_manquant = ProduitManquant(NOM_DE_PRODUIT_MANQUANT)

        self.produit_manquant_service.signale(NOM_DE_PRODUIT_MANQUANT)

        self.produit_manquant_repository.ajoute.assert_called_with(produit_manquant)

    def test_renvoie_une_erreur_quand_le_produit_est_inconnu(self):
        self.produit_manquant_repository.est_un_nom_de_produit_connu.return_value = False

        with pytest.raises(ProduitInconnuException):
            self.produit_manquant_service.signale(NOM_DE_PRODUIT_INCONNU)

    def test_lister_les_produits_manquants(self):
        self.produit_manquant_repository.liste_des_produits_manquants.return_value = \
            [PRODUIT_MANQUANT]

        assert [PRODUIT_MANQUANT] == self.produit_manquant_service.liste_des_produits_manquants()

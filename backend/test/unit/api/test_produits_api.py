import json
from unittest.mock import Mock

from il_manque_du_beurre.domaine.produit_inconnu_exception import ProduitInconnuException
from il_manque_du_beurre.domaine.produit_manquant import ProduitManquant
from il_manque_du_beurre.domaine.produit_manquant_service import ProduitManquantService
from il_manque_du_beurre.infrastructure.api.produits_api import ProduitsAPI

NOM_DE_PRODUIT_CONNU = 'beurre'
NOM_DE_PRODUIT_INCONNU = 'poivron bleu'
PRODUIT_MANQUANT = ProduitManquant(NOM_DE_PRODUIT_CONNU)


class TestProduitAPI:
    def setup_method(self):
        self.produit_manquant_service = Mock(ProduitManquantService)
        self.produits_api = ProduitsAPI(self.produit_manquant_service)

    def test_renvoie_200_quand_on_signale_qu_un_produit_est_manquant(self):
        response = self.produits_api.signaler_produit_manquant(NOM_DE_PRODUIT_CONNU)

        self.produit_manquant_service.signale_manquant.assert_called_with(NOM_DE_PRODUIT_CONNU)
        assert response.data == b''
        assert response.status == '200 OK'
        assert response.mimetype == 'application/json'

    def test_renvoie_une_erreur_quand_un_produit_est_inconnu(self):
        self.produit_manquant_service.signale_manquant.side_effect = \
            ProduitInconnuException(NOM_DE_PRODUIT_INCONNU)

        response = self.produits_api.signaler_produit_manquant(NOM_DE_PRODUIT_INCONNU)

        assert response.data == json_contenant({
            'erreur': {
                'description': 'Produit inconnu : "poivron bleu"'
            }
        })
        assert response.status == '400 BAD REQUEST'
        assert response.mimetype == 'application/json'

    def test_renvoie_la_liste_des_produits_manquants(self):
        self.produit_manquant_service.liste_des_produits_manquants.return_value = \
            [PRODUIT_MANQUANT]

        response = self.produits_api.liste_des_produits_manquants()

        assert response.data == json_contenant([{'nom': 'beurre'}])
        assert response.status == '200 OK'
        assert response.mimetype == 'application/json'

    def test_signaler_qu_un_produit_n_est_plus_manquant(self):

        response = self.produits_api.signaler_produit_non_manquant(NOM_DE_PRODUIT_CONNU)

        self.produit_manquant_service.signale_non_manquant.assert_called_with(NOM_DE_PRODUIT_CONNU)
        assert response.data == b''
        assert response.status == '200 OK'
        assert response.mimetype == 'application/json'

    def test_renvoie_une_erreur_quand_un_produit_inconnu_est_signale_non_manquant(self):
        self.produit_manquant_service.signale_non_manquant.side_effect = \
            ProduitInconnuException(NOM_DE_PRODUIT_INCONNU)

        response = self.produits_api.signaler_produit_non_manquant(NOM_DE_PRODUIT_INCONNU)

        assert response.data == json_contenant({
            'erreur': {
                'description': 'Produit inconnu : "poivron bleu"'
            }
        })
        assert response.status == '400 BAD REQUEST'
        assert response.mimetype == 'application/json'


def json_contenant(structure):
    return bytes(json.dumps(structure), encoding='utf-8')

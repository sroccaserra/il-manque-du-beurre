from flask import Blueprint

from il_manque_du_beurre.application.produits_api import ProduitAPI
from il_manque_du_beurre.domaine.produit_manquant_service import ProduitManquantService

api = Blueprint('API', __name__, url_prefix='/api')


@api.route('/produits_manquants/<nom_de_produit>', methods=['POST'])
def produits(nom_de_produit):
    produit_manquant_service = ProduitManquantService()
    produit_api = ProduitAPI(produit_manquant_service)
    return produit_api.signaler_produit_manquant(nom_de_produit)

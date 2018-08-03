from flask import Blueprint

from il_manque_du_beurre.application.produits_api import ProduitsAPI
from il_manque_du_beurre.domaine.produit_manquant_repository import ProduitManquantRepository
from il_manque_du_beurre.domaine.produit_manquant_service import ProduitManquantService

api = Blueprint('API', __name__, url_prefix='/api')

produit_manquant_repository = ProduitManquantRepository()
produit_manquant_service = ProduitManquantService(produit_manquant_repository)
produits_api = ProduitsAPI(produit_manquant_service)


@api.route('/produits_manquants', methods=['GET'])
def lister_produits_manquants():
    return produits_api.liste_des_produits_manquants()


@api.route('/produits_manquants/<nom_de_produit>', methods=['POST'])
def signaler_un_produit_manquant(nom_de_produit):
    return produits_api.signaler_produit_manquant(nom_de_produit)

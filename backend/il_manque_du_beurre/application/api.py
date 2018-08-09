from flask import Blueprint

from il_manque_du_beurre.application.bootstrap import produits_api

api = Blueprint('API', __name__, url_prefix='/api')


@api.route('/produits_manquants', methods=['GET'])
def lister_produits_manquants():
    return produits_api.liste_des_produits_manquants()


@api.route('/produits_manquants/<nom_de_produit>', methods=['POST'])
def signaler_un_produit_manquant(nom_de_produit):
    return produits_api.signaler_produit_manquant(nom_de_produit)


@api.route('/produits_manquants/<nom_de_produit>', methods=['DELETE'])
def signaler_un_produit_non_manquant(nom_de_produit):
    return produits_api.signaler_produit_non_manquant(nom_de_produit)

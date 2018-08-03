import json
from http import HTTPStatus

from il_manque_du_beurre.domaine.produit_inconnu_exception import ProduitInconnuException


class ProduitsAPI:
    def __init__(self, produit_manquant_service):
        self.produit_manquant_service = produit_manquant_service

    def signaler_produit_manquant(self, nom_de_produit_manquant):
        try:
            self.produit_manquant_service.signale(nom_de_produit_manquant)
            return '', HTTPStatus.OK
        except ProduitInconnuException:
            message = 'Produit inconnu : "{0}"'.format(nom_de_produit_manquant)
            return message, HTTPStatus.BAD_REQUEST

    def liste_des_produits_manquants(self):
        produits_manquants = self.produit_manquant_service.liste_des_produits_manquants()
        response_body = self.json_contenant(produits_manquants)
        return response_body, HTTPStatus.OK

    def json_contenant(self, liste_de_produits_manquants):
        return json.dumps([{"nom": produit.nom} for produit in liste_de_produits_manquants])

from http import HTTPStatus

from flask import Response

from il_manque_du_beurre.application.json.erreur_json import serialise_erreur
from il_manque_du_beurre.application.json.produits_json import serialise_liste
from il_manque_du_beurre.domaine.produit_inconnu_exception import ProduitInconnuException


class ProduitsAPI:
    def __init__(self, produit_manquant_service):
        self.produit_manquant_service = produit_manquant_service

    def signaler_produit_manquant(self, nom_de_produit_manquant):
        try:
            self.produit_manquant_service.signale(nom_de_produit_manquant)
            return Response('',
                            status=HTTPStatus.OK,
                            mimetype='application/json')

        except ProduitInconnuException:
            message_d_erreur = 'Produit inconnu : "{0}"'.format(nom_de_produit_manquant)
            return Response(serialise_erreur(message_d_erreur),
                            status=HTTPStatus.BAD_REQUEST,
                            mimetype='application/json')

    def liste_des_produits_manquants(self):
        produits_manquants = self.produit_manquant_service.liste_des_produits_manquants()
        response_body = serialise_liste(produits_manquants)
        return Response(response_body,
                        status=HTTPStatus.OK,
                        mimetype='application/json')

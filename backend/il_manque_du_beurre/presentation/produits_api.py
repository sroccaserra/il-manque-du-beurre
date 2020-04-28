from http import HTTPStatus

from flask import Response

from il_manque_du_beurre.presentation.json.erreur_json import serialise_erreur
from il_manque_du_beurre.presentation.json.produits_json import serialise_liste
from il_manque_du_beurre.domaine.produit_inconnu_exception import ProduitInconnuException


def bad_request_json_response(message):
    return Response(serialise_erreur(message),
                    status=HTTPStatus.BAD_REQUEST,
                    mimetype='application/json')


def ok_json_response(body):
    return Response(body,
                    status=HTTPStatus.OK,
                    mimetype='application/json')


class ProduitsAPI:
    def __init__(self, produit_manquant_service):
        self.produit_manquant_service = produit_manquant_service

    def signaler_produit_manquant(self, nom_de_produit_connu):
        try:
            self.produit_manquant_service.signale_manquant(nom_de_produit_connu)
            return ok_json_response('')

        except ProduitInconnuException:
            message_d_erreur = 'Produit inconnu : "{0}"'.format(nom_de_produit_connu)
            return bad_request_json_response(message_d_erreur)

    def signaler_produit_non_manquant(self, nom_de_produit_connu):
        try:
            self.produit_manquant_service.signale_non_manquant(nom_de_produit_connu)
            return ok_json_response('')

        except ProduitInconnuException:
            message_d_erreur = 'Produit inconnu : "{0}"'.format(nom_de_produit_connu)
            return bad_request_json_response(message_d_erreur)

    def liste_des_produits_manquants(self):
        produits_manquants = self.produit_manquant_service.liste_des_produits_manquants()
        response_body = serialise_liste(produits_manquants)
        return ok_json_response(response_body)

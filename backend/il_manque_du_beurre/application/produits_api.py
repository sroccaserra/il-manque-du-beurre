from http import HTTPStatus

from il_manque_du_beurre.domaine.produit_manquant import ProduitManquant


class ProduitAPI:
    def __init__(self, produit_manquant_service):
        self.produit_manquant_service = produit_manquant_service

    def signaler_produit_manquant(self, nom_de_produit_manquant):
        produit_manquant = ProduitManquant.de_nom(nom_de_produit_manquant)
        self.produit_manquant_service.signale(produit_manquant)
        return "", HTTPStatus.CREATED

from il_manque_du_beurre.domaine.produit_inconnu_exception import ProduitInconnuException
from il_manque_du_beurre.domaine.produit_manquant import ProduitManquant

PRODUITS_CONNUS = ['beurre']


class ProduitManquantService:
    def __init__(self, produit_manquant_repository):
        self.produit_manquant_repository = produit_manquant_repository

    def signale(self, nom_de_produit_manquant):
        self.valide(nom_de_produit_manquant)
        produit_manquant = ProduitManquant(nom_de_produit_manquant)
        self.produit_manquant_repository.ajoute(produit_manquant)

    def valide(self, nom_de_produit_manquant):
        if nom_de_produit_manquant not in PRODUITS_CONNUS:
            raise ProduitInconnuException(nom_de_produit_manquant)

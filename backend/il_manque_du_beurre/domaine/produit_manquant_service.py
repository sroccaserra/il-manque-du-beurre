from il_manque_du_beurre.domaine.produit_inconnu_exception import ProduitInconnuException
from il_manque_du_beurre.domaine.produit_manquant import ProduitManquant


class ProduitManquantService:
    def __init__(self, produit_manquant_repository):
        self.repository = produit_manquant_repository

    def signale(self, nom_de_produit_manquant):
        self.valide_nom_de_produit(nom_de_produit_manquant)
        produit_manquant = ProduitManquant(nom_de_produit_manquant)
        self.repository.ajoute(produit_manquant)

    def valide_nom_de_produit(self, nom_de_produit_manquant):
        if not self.repository.est_un_nom_de_produit_connu(nom_de_produit_manquant):
            raise ProduitInconnuException(nom_de_produit_manquant)

    def liste_des_produits_manquants(self):
        return self.repository.liste_des_produits_manquants()

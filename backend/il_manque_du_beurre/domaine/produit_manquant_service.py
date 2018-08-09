from il_manque_du_beurre.domaine.produit_inconnu_exception import ProduitInconnuException
from il_manque_du_beurre.domaine.produit_manquant import ProduitManquant


class ProduitManquantService:
    def __init__(self, produit_manquant_repository):
        self.repository = produit_manquant_repository

    def signale_manquant(self, nom_de_produit_connu):
        self._valide_nom_de_produit(nom_de_produit_connu)
        produit_manquant = ProduitManquant(nom_de_produit_connu)
        self.repository.ajoute(produit_manquant)

    def signale_non_manquant(self, nom_de_produit_connu):
        self._valide_nom_de_produit(nom_de_produit_connu)
        produit_manquant = ProduitManquant(nom_de_produit_connu)
        self.repository.retire(produit_manquant)

    def liste_des_produits_manquants(self):
        return self.repository.liste_des_produits_manquants()

    def _valide_nom_de_produit(self, nom_de_produit):
        if not self.repository.est_un_nom_de_produit_connu(nom_de_produit):
            raise ProduitInconnuException(nom_de_produit)

NOMS_DE_PRODUITS_CONNUS = ['beurre']


class ProduitManquantRepository:
    def __init__(self):
        self.produits_manquants = []

    def ajoute(self, produit_manquant):
        self.produits_manquants.append(produit_manquant)

    def est_un_nom_de_produit_connu(self, nom_de_produit):
        return nom_de_produit in NOMS_DE_PRODUITS_CONNUS

    def liste_des_produits_manquants(self):
        return self.produits_manquants

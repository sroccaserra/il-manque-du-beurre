from il_manque_du_beurre.domaine.produit_manquant_repository import ProduitManquantRepository


class ProduitManquantSqlRepository(ProduitManquantRepository):
    def __init__(self, data_store):
        super().__init__()
        self.data_store = data_store

    def ajoute(self, produit_manquant):
        raise NotImplementedError()

    def est_un_nom_de_produit_connu(self, nom_de_produit):
        raise NotImplementedError()

    def liste_des_produits_manquants(self):
        raise NotImplementedError()

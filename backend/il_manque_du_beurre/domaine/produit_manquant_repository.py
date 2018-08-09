from il_manque_du_beurre.domaine.produit_manquant import ProduitManquant


class ProduitManquantRepository:
    def ajoute(self, produit_manquant: ProduitManquant) -> None:
        raise NotImplementedError()

    def est_un_nom_de_produit_connu(self, nom_de_produit: str) -> bool:
        raise NotImplementedError()

    def liste_des_produits_manquants(self) -> [ProduitManquant]:
        raise NotImplementedError()

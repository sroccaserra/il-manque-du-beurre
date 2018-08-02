class ProduitManquantService:
    def __init__(self, produit_manquant_repository):
        self.produit_manquant_repository = produit_manquant_repository

    def signale(self, produit_manquant):
        self.produit_manquant_repository.ajoute(produit_manquant)

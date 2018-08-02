class ProduitInconnuException(Exception):
    def __init__(self, nom_de_produit):
        self.nom_de_produit = nom_de_produit

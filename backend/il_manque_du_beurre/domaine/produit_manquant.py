class ProduitManquant:
    def __init__(self, nom):
        self.nom = nom

    def __eq__(self, other):
        return self.nom == other.nom

class ProduitManquant:
    def __init__(self, nom):
        self.nom = nom

    def __eq__(self, other):
        return self.nom == other.nom

    @staticmethod
    def de_nom(nom):
        return ProduitManquant(nom)

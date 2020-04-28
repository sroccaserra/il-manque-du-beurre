import json


def serialise_liste(liste_de_produits_manquants):
    return json.dumps([
        {"nom": produit.nom}
        for produit in liste_de_produits_manquants
    ])

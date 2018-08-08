from il_manque_du_beurre.domaine.produit_manquant import ProduitManquant

from il_manque_du_beurre.domaine.produit_manquant_repository import ProduitManquantRepository


def _deserialize_en_produits_manquants(rows):
    return [ProduitManquant(row.nom) for row in rows]


class ProduitManquantSqlRepository(ProduitManquantRepository):
    def __init__(self, data_store):
        super().__init__()
        self.data_store = data_store

    def ajoute(self, produit_manquant):
        sql_query = '''
        INSERT INTO produits_manquants(nom)
        VALUES (:nom)
        '''
        self.data_store.execute(sql_query, {'nom': produit_manquant.nom})

    def est_un_nom_de_produit_connu(self, nom_de_produit):
        raise NotImplementedError()

    def liste_des_produits_manquants(self):
        sql_query = '''
        SELECT nom FROM produits_manquants
        '''
        result_set = self.data_store.execute(sql_query)
        rows = result_set.fetchall()
        return _deserialize_en_produits_manquants(rows)

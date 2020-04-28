from il_manque_du_beurre.presentation.produits_api import ProduitsAPI
from il_manque_du_beurre.domaine.produit_manquant_service import ProduitManquantService
from il_manque_du_beurre.infrastructure.database.data_store import DataStore
from il_manque_du_beurre.infrastructure.produit_manquant.produit_manquant_sql_repository import \
    ProduitManquantSqlRepository
from il_manque_du_beurre.settings import DATABASE_USER, DATABASE_PASSWORD, DATABASE_HOST, \
    DATABASE_PORT, DATABASE_NAME

data_store = DataStore(DATABASE_USER,
                       DATABASE_PASSWORD,
                       DATABASE_HOST,
                       DATABASE_PORT,
                       DATABASE_NAME)
produit_manquant_repository = ProduitManquantSqlRepository(data_store)
produit_manquant_service = ProduitManquantService(produit_manquant_repository)
produits_api = ProduitsAPI(produit_manquant_service)

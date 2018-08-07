from il_manque_du_beurre.infrastructure.database.data_store import DataStore
from il_manque_du_beurre.settings import DATABASE_USER, DATABASE_PASSWORD, DATABASE_HOST, \
    DATABASE_PORT, DATABASE_TEST_NAME


def data_store_for_tests():
    return DataStore(DATABASE_USER,
                     DATABASE_PASSWORD,
                     DATABASE_HOST,
                     DATABASE_PORT,
                     DATABASE_TEST_NAME)

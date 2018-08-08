from il_manque_du_beurre.infrastructure.database.data_store import DataStore
from il_manque_du_beurre.settings import DATABASE_USER, DATABASE_PASSWORD, DATABASE_HOST, \
    DATABASE_PORT, DATABASE_TEST_NAME


class DatabaseTestBaseClass:
    def setup_method(self):
        self.data_store = DataStore(DATABASE_USER,
                                    DATABASE_PASSWORD,
                                    DATABASE_HOST,
                                    DATABASE_PORT,
                                    DATABASE_TEST_NAME)
        self.data_store.clear_all_tables()

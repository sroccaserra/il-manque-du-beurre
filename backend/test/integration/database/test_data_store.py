from il_manque_du_beurre.infrastructure.database.data_store import DataStore
from il_manque_du_beurre.settings import DATABASE_USER, DATABASE_PASSWORD, DATABASE_HOST, \
    DATABASE_PORT, DATABASE_NAME


class TestDataStore:
    def test_data_store(self):
        data_store = DataStore(DATABASE_USER,
                               DATABASE_PASSWORD,
                               DATABASE_HOST,
                               DATABASE_PORT,
                               DATABASE_NAME)

        result_set = data_store.execute('select 1')
        rows = result_set.fetchall()

        assert (1,) == rows[0]

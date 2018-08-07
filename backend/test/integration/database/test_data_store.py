from test.integration.database.data_store_for_tests import data_store_for_tests


class TestDataStore:
    def test_data_store(self):
        data_store = data_store_for_tests()

        result_set = data_store.execute('select 1')
        rows = result_set.fetchall()

        assert (1,) == rows[0]

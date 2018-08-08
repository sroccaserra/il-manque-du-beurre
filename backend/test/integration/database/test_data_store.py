from test.integration.database.database_test_base_class import DatabaseTestBaseClass


class TestDataStore(DatabaseTestBaseClass):
    def test_data_store(self):
        result_set = self.data_store.execute('select 1')
        rows = result_set.fetchall()

        assert (1,) == rows[0]

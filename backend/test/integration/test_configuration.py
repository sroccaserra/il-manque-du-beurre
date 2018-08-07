from il_manque_du_beurre.settings import DATABASE_NAME


class TestConfiguration:
    def test_database_name(self):
        assert DATABASE_NAME == 'postgres'

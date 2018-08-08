from sqlalchemy import create_engine, text, MetaData


class DataStore:
    def __init__(self, user, password, host, port, database):
        connection_string = 'postgresql+psycopg2://{0}:{1}@{2}:{3}/{4}'.format(user,
                                                                               password,
                                                                               host,
                                                                               port,
                                                                               database)
        self.engine = create_engine(connection_string)

    def execute(self, statement, arguments=None):
        if arguments is None:
            arguments = {}
        connection = self.engine.connect()
        query = text(statement)
        return connection.execute(query, **arguments)

    def clear_all_tables(self):
        metadata = MetaData(bind=self.engine)
        metadata.reflect()
        clear_table_connection = self.engine.connect()
        transaction = clear_table_connection.begin()
        for table in reversed(metadata.sorted_tables):
            if table.name not in ['produits_connus', 'alembic_version']:
                clear_table_connection.execute(table.delete())
        transaction.commit()
        clear_table_connection.close()

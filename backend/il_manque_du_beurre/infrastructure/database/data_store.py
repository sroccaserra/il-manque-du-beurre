from sqlalchemy import create_engine, text


class DataStore:
    def __init__(self, user, password, host, port, database):
        connection_string = 'postgresql+psycopg2://{0}:{1}@{2}:{3}/{4}'.format(user,
                                                                               password,
                                                                               host,
                                                                               port,
                                                                               database)
        self.engine = create_engine(connection_string)

    def execute(self, statement):
        connection = self.engine.connect()
        query = text(statement)
        return connection.execute(query)

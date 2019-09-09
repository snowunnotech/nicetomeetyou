import sqlalchemy


class PostgresProvider(object):

    def __init__(self):
        self.connection = None
        self.meta = None

    def connect(self, user, password, db, host='localhost', port=5432):
        url = 'postgresql+psycopg2://{}:{}@{}:{}/{}'
        url = url.format(user, password, host, port, db)

        self.connection = sqlalchemy.create_engine(url, client_encoding='utf8')

        self.meta = sqlalchemy.MetaData(bind=self.connection, reflect=True)


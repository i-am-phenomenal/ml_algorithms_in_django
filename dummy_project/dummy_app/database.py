import sqlalchemy as sql

class Database():
    engine = sql.create_engine(
        'postgresql://postgres:postgres@127.0.0.1/django_database')

    def __init__(self):
        self.connection = self.engine.connect()
        print("Database Instance Created ")

    def fetch_all_records(self, tablename):
        fetch_query = self.connection.execute(f"SELECT * FROM {tablename}")
        for record in fetch_query.fetchall():
            print(record)

    def fetch_records_by_id(self, id, tablename):
        fetch_query = self.connection.execute(
            f"SELECT * FROM {tablename} WHERE ID = {id}")
        fetched_record = fetch_query.fetchall()
        print(fetched_record)

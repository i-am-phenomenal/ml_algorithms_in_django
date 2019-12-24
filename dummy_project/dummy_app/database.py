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

    def fetch_names_from_given_character(self, character):
        fetch_query = self.connection.execute(
            f"SELECT * FROM nasa_dataset WHERE NAME LIKE '{character}%%'")

        return fetch_query.fetchall()
        # print()

    def get_distinct_fall(self):
        query = self.connection.execute(
            f"select distinct fall from nasa_dataset"
        )

        print(query.fetchall())

    def get_record_by_fall_type(self, fall_type):
        fetch_query = self.connection.execute(
            f"select * from nasa_dataset where fall = '{fall_type}'"
        )

        for record in fetch_query.fetchall():
            print(record)

    def get_negative_reclongs(self):
        query = self.connection.execute(
            f"select * from nasa_dataset where reclong < 0"
        )

        print(query.fetchall())

    def get_sum_of_all_reclongs(self):
        query = self.connection.execute(
            f"select sum(reclong) from nasa_dataset"
        )

        print(query.fetchall())

    def get_sum_of_negative_reclongs(self):
        query = self.connection.execute(
            f" select sum(reclong) from nasa_dataset where reclong < 0"
        )

        print(query.fetchall())

    def get_distinct_nametype(self):
        query = self.connection.execute(
            f"select distinct nametype from nasa_dataset"
        )

        print(query.fetchall())

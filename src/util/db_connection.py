from peewee import SqliteDatabase


class DbConnection:
    _sqlitedb = None
    _name = "k9tax_db"

    @classmethod
    def get_sqlite_file_db(cls):
        if cls._sqlitedb is None:
            cls._sqlitedb = SqliteDatabase(cls._name)
        return cls._sqlitedb

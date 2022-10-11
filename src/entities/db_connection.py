from peewee import SqliteDatabase

class DbConnection:
    SqliteFileDb = None
    name = "k9tax_db"
    
    @classmethod
    def get_sqllite_file_db(cls):
        if cls.SqliteFileDb is None:
            cls.SqliteFileDb = SqliteDatabase("k9tax_db")
        return cls.SqliteFileDb
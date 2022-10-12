from peewee import *
from src.util.db_connection import DbConnection

class BaseModel(Model):
    class Meta:
        database = DbConnection.get_sqlite_file_db()
import sqlite3
from peewee import *

def setup_staging(pw_db):
    connection = pw_db.connection()
    connection.execute("CREATE TABLE IF NOT EXISTS stg_Breed (name STRING, breed_group STRING, popularity STRING);")
    connection.commit()


if __name__ == '__main__':
    pw_db = SqliteDatabase('k9tax_db')
    setup_staging(pw_db)

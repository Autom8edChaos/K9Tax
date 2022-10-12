import os
import pytest
from src.util.setup import setup_staging
from src.util.db_connection import DbConnection
from peewee import SqliteDatabase

@pytest.fixture(scope='module')
def pw_db():
    db_name = DbConnection._name 
    if os.path.exists(db_name):
        os.remove(db_name)
    
    db = DbConnection.get_sqlite_file_db()
    db.connect()
    
    yield db

    db.commit()
    db.close()
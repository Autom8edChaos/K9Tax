import os
import pytest
from src.util.setup import setup_staging
from peewee import SqliteDatabase

@pytest.fixture(scope='module')
def pw_db():
    db_name = 'k9tax_db'
    if os.path.exists(db_name):
        os.remove(db_name)
    db = SqliteDatabase(db_name)
    db.connect()
    setup_staging(db)
    yield db
    db.close()
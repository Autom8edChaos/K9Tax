import os
import pytest
import sqlite3
from src.loading.breedloader import BreedLoader
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

def test_can_load_data_in_staging(pw_db):
    loader = BreedLoader(pw_db)
    loader.load_staging('test/integration/data/breeds.csv')
    cursor = pw_db.connection().execute('SELECT * FROM stg_Breed')
    assert len(cursor.fetchall()) == 26
    
def test_can_load_data_from_staging_to_raw(pw_db):
    loader = BreedLoader(pw_db)
    loader.load_staging('test/integration/data/breeds.csv')
    loader.load_raw()
    cursor = pw_db.connection().execute('SELECT * FROM DogBreed')
    assert len(cursor.fetchall()) == 26
    


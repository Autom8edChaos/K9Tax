import os
import pytest
from src.util.setup import setup_staging
from src.entities.db_connection import DbConnection
from src.entities.dog_breed import DogBreed, Dog
from peewee import SqliteDatabase

@pytest.fixture(scope='module')
def pw_db():
    db_name = DbConnection.name 
    if os.path.exists(db_name):
        os.remove(db_name)
    db = DbConnection.get_sqllite_file_db()
    
    db.connect()
    db.create_tables([DogBreed])
    db.create_tables([Dog])
    
    #setup_staging(db)
    yield db
    db.commit()
    db.close()
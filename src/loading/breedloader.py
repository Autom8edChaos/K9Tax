import pandas as pd
from src.entities.dog_breed import DogBreed, Dog
from abc import ABC, abstractmethod
from peewee import *


class StagingLoader(ABC):
    def __init__(self, name_stg, peewee_db):
        self.pw_db = peewee_db
        self.connection = peewee_db.connection()
        self.name_stg = name_stg

    def load_staging(self, source):
        data = pd.read_csv(source)
        self._load_staging_data(data)
        
    def _load_staging_data(self, data):
        data.to_sql(self.name_stg, self.connection, if_exists='replace', index=False)
        
    def _fetch_all(self, columns: list):
        cursor = self.connection.execute(
            f'SELECT {",".join(columns)} FROM {self.name_stg}'
        )
        return cursor.fetchall()


class RawLoader():
    def _load_raw(self, model):
        db = self.pw_db
        #db.create_tables([model])
        
        data = self._fetch_all(self.col_mapping.keys())
        fields = self.col_mapping.values()
        with db.atomic() as txn:
            model.insert_many(data, fields=fields).execute()
            txn.commit()
        

class BreedLoader(StagingLoader, RawLoader):
    col_mapping = {
        'name': DogBreed.name,
        'breed_group': DogBreed.breed_group,
        'popularity': DogBreed.popularity
    }
    
    def __init__(self, peewee_database):
        super().__init__('stg_Breed', peewee_database)

    def load_raw(self):
        self._load_raw(DogBreed)

       

class DogLoader(StagingLoader, RawLoader):
    col_mapping = {
        'naam': Dog.name,
        'id': Dog.id,
        'eigenaar_bsn': Dog.owner_bsn,
        'ras': Dog.breed,
        'GeboorteDatum': Dog.date_of_birth,
        'SterfteDatum': Dog.date_of_death
    }
    
    def __init__(self, peewee_database):
        super().__init__('stg_Dog', peewee_database)

    def load_raw(self):
        self._load_raw(Dog)
        
    
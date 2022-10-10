import pandas as pd
from src.entities.dog_breed import DogBreed
from peewee import *

class BreedLoader():
    name_stg = 'stg_Breed'
    name_raw = 'raw_Breed'
    columns = ['name', 'breed_group', 'popularity']
    
    def __init__(self, peewee_database):
        self.pw_db = peewee_database
        self.connection = peewee_database.connection()

    def load_staging(self, source):
        data = pd.read_csv(source)
        self._load_staging_data(data)
        
    def _load_staging_data(self, data):
        data.to_sql(self.name_stg, self.connection, if_exists='replace', index=False)

    def load_raw(self):
        db = self.pw_db
        db.create_tables([DogBreed])
        
        cursor = self.connection.execute(
            f'SELECT {",".join(self.columns)} FROM {self.name_stg}'
        )
        breeds = cursor.fetchall()
        breed_objects = [DogBreed.create(name=breed[0], breed_group=breed[1], popularity=breed[2]) for breed in breeds]

        [breed_object.save() for breed_object in breed_objects]
        


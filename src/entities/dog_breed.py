from peewee import *
from dataclasses import dataclass
from src.entities.db_connection import DbConnection

# db = SqliteDatabase('k9tax_db')

#@dataclass
class BaseModel(Model):
    class Meta:
        database = DbConnection.get_sqllite_file_db()

class DogBreed(BaseModel):
    name = TextField()
    breed_group = TextField()
    popularity = IntegerField()

class Dog(BaseModel):
    name = TextField()
    id = IntegerField(null = True)
    owner_bsn = TextField()
    breed = TextField()
    date_of_birth = TextField()
    date_of_death = TextField(null = True)
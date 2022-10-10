from peewee import *
from dataclasses import dataclass

db = SqliteDatabase('k9tax_db')

#@dataclass
class BaseModel(Model):
    class Meta:
        database = db

class DogBreed(BaseModel):
    name = TextField()
    breed_group = TextField()
    popularity = IntegerField()

class Dog(BaseModel):
    name = TextField()
    id = IntegerField()
    owner_bsn = TextField()
    breed = TextField()
    date_of_birth = TextField()
    date_of_death = TextField()
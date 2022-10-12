from peewee import *
from src.entities.base_model import BaseModel


class Dog(BaseModel):
    name = TextField()
    id = IntegerField(null = True)
    owner_bsn = TextField()
    breed = TextField()
    date_of_birth = TextField()
    date_of_death = TextField(null = True)
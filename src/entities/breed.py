from peewee import *
from src.entities.base_model import BaseModel


class Breed(BaseModel):
    name = TextField(unique=True)
    breed_group = TextField()
    popularity = IntegerField()


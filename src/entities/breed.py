from peewee import *
from src.entities.base_model import BaseModel


class Breed(BaseModel):
    name = TextField()
    breed_group = TextField()
    popularity = IntegerField()


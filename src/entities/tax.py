from peewee import *
from src.entities.base_model import BaseModel


class Tax(BaseModel):
    breed = TextField()
    payment = DecimalField()
    
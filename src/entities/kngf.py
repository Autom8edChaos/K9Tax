from peewee import *
from src.entities.base_model import BaseModel


class Kngf(BaseModel):
    name = TextField()
    id = DecimalField()
    type = DecimalField()
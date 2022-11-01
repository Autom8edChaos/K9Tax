from peewee import *
from src.entities.base_model import BaseModel


class Owner(BaseModel):
    name = TextField()
    street = TextField()
    house_number = TextField()
    zipcode = TextField()
    place = TextField()
    bsn = TextField()
    disctrict_code = TextField()
    
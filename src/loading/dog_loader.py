from src.entities.dog import Dog
from src.loading.loaders import Loader

class DogLoader(Loader):
    model = Dog
    col_mapping = {
        'naam': model.name,
        'id': model.id,
        'eigenaar_bsn': model.owner_bsn,
        'ras': model.breed,
        'GeboorteDatum': model.date_of_birth,
        'SterfteDatum': model.date_of_death
    }
    
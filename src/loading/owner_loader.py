from src.entities.owner import Owner
from src.loading.loaders import Loader

class OwnerLoader(Loader):
    model = Owner
    col_mapping = {
        'Naam': model.name,
        'straatnaam': model.street,
        'huisnummer': model.house_number,
        'postcode': model.zipcode,
        'plaats': model.place,
        'BSN': model.bsn,
        'Wijkcode': model.disctrict_code,
    }

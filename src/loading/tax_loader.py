from src.entities.tax import Tax
from src.loading.loaders import Loader

class TaxLoader(Loader):
    model = Tax
    col_mapping = {
        'ras': model.breed,
        'kwartaalbedrag': model.payment
    }

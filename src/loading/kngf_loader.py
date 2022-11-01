from src.entities.kngf import Kngf
from src.loading.loaders import Loader

class KngfLoader(Loader):
    model = Kngf
    col_mapping = {
        'Naam': model.name,
        'ID': model.id,
        'Type': model.type,
    }

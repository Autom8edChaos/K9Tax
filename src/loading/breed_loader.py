from src.entities.breed import Breed
from src.loading.loaders import Loader

class BreedLoader(Loader):
    model = Breed
    col_mapping = {
        'name': model.name,
        'breed_group': model.breed_group,
        'popularity': model.popularity
    }
    



       


        
    
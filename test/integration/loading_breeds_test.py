from src.loading.breedloader import BreedLoader

def test_can_load_data_in_staging(pw_db):
    loader = BreedLoader(pw_db)
    loader.load_staging('test/integration/data/breeds.csv')
    cursor = pw_db.connection().execute('SELECT * FROM stg_Breed')
    assert len(cursor.fetchall()) == 26
    
def test_can_load_data_from_staging_to_raw(pw_db):
    loader = BreedLoader(pw_db)
    loader.load_staging('test/integration/data/breeds.csv')
    loader.load_raw()
    cursor = pw_db.connection().execute('SELECT * FROM DogBreed')
    assert len(cursor.fetchall()) == 26
    


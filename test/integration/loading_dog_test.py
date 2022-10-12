from src.loading.dog_loader import DogLoader

def test_can_load_dog_data_in_staging(pw_db):
    loader = DogLoader(pw_db)
    loader.load_staging('test/integration/data/dogs.csv')
    cursor = pw_db.connection().execute('SELECT * FROM stg_Dog')
    assert len(cursor.fetchall()) == 20
    
def test_can_load_data_from_staging_to_raw(pw_db):
    loader = DogLoader(pw_db)
    loader.load_staging('test/integration/data/dogs.csv')
    loader.load_raw()
    cursor = pw_db.connection().execute('SELECT * FROM Dog')
    assert len(cursor.fetchall()) == 20




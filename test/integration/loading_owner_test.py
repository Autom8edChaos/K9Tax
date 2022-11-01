from src.loading.owner_loader import OwnerLoader

def test_can_load_data_in_staging(pw_db):
    loader = OwnerLoader(pw_db)
    loader.load_staging('test/integration/data/eigenaar.csv')
    cursor = pw_db.connection().execute('SELECT * FROM stg_owner')
    assert len(cursor.fetchall()) == 20
    
def test_can_load_data_from_staging_to_raw(pw_db):
    loader = OwnerLoader(pw_db)
    loader.load_staging('test/integration/data/eigenaar.csv')
    loader.load_raw()
    cursor = pw_db.connection().execute('SELECT * FROM Owner')
    assert len(cursor.fetchall()) == 20


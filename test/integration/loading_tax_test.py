from src.loading.tax_loader import TaxLoader

def test_can_load_data_in_staging(pw_db):
    loader = TaxLoader(pw_db)
    loader.load_staging('test/integration/data/belasting.csv')
    cursor = pw_db.connection().execute('SELECT * FROM stg_Tax')
    assert len(cursor.fetchall()) == 26
    
def test_can_load_data_from_staging_to_raw(pw_db):
    loader = TaxLoader(pw_db)
    loader.load_staging('test/integration/data/belasting.csv')
    loader.load_raw()
    cursor = pw_db.connection().execute('SELECT * FROM Tax')
    assert len(cursor.fetchall()) == 26


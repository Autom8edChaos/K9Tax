from src.loading.kngf_loader import KngfLoader

def test_can_load_data_in_staging(pw_db):
    loader = KngfLoader(pw_db)
    loader.load_staging('test/integration/data/KNGF.csv')
    cursor = pw_db.connection().execute('SELECT * FROM stg_Kngf')
    assert len(cursor.fetchall()) == 15
    
def test_can_load_data_from_staging_to_raw(pw_db):
    loader = KngfLoader(pw_db)
    loader.load_staging('test/integration/data/KNGF.csv')
    loader.load_raw()
    cursor = pw_db.connection().execute('SELECT * FROM Kngf')
    assert len(cursor.fetchall()) == 15


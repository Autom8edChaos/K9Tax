from src.import_dog import CsvLoader


def test_import_of_clean_file():
    csv_loader = CsvLoader
    dogs = csv_loader.LoadDogs('hond.csv')
    
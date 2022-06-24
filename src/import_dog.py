import csv
from dataclasses import dataclass

@dataclass
class Dog():
    id: str = None
    eigenaar_bsn: str = None
    naam: str = None
    ras: str = None
    geboortedatum: str = None
    sterftedatum: str = None 

class CsvLoader():
    
    def LoadDogs(self, filename: str) -> list:
        with open(filename, "r") as f:
            reader = csv.DictReader(f)
            dogs = list(reader)
            
        return [Dog(**dog_spec) for dog_spec in dogs]
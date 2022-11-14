import pytest
from src.logic.dog_breed_logic import DogBreedLogic

@pytest.mark.parametrize('given,real', [
    ('bouvier', 'bouvier'),
    ('boevier', 'bouvier'),
    ('boefjee', 'bouvier'),
    ('Boefje' , 'onbekend'),
])
def test_can_get_best_matching_dog_breed_requirements_check(given, real):
    assert DogBreedLogic().try_get_breed(given) == real


# Run with: python -m pytest test/unit/*requirement.py

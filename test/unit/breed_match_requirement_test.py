import pytest
from src.logic.dog_breed_logic import DogBreedLogic

@pytest.fixture
def breedlist():
    return ['boxer', 'mastiff', 'bouvier']

@pytest.mark.parametrize('given,real', [
    pytest.param('bouvier', 'bouvier'),
    pytest.param('boevier', 'bouvier'),
    pytest.param('boefjee', 'bouvier'),
    pytest.param('Boefje', 'onbekend'),
])
def test_can_get_best_matching_dog_breed_requirements_check(breedlist, given, real):
    assert DogBreedLogic(breedlist).try_get_breed(given) == real

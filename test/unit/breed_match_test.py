import pytest
from src.logic.dog_breed_logic import DogBreedLogic

@pytest.mark.parametrize('given,real,prob', [
    pytest.param('boxer', 'boxer', 0, id='exact match'),
    pytest.param('BOXER', 'boxer', 0, id='case insensitive match'),
    pytest.param('bokser', 'boxer', 2, id='near match'),
    pytest.param('Mastiff', 'boxer', 7, id='mismatch'),
    pytest.param('Boceron', 'beauceron', 3, id='variant'),
    pytest.param('Boefjee', 'bouvier', 4, id='variant'),
])
def test_can_get_probability_for_dog_breed(given, real, prob):
    assert DogBreedLogic.get_probability(given, real) == prob


@pytest.fixture
def breedlist():
    return ['boxer', 'mastiff', 'bouvier']

@pytest.mark.parametrize('given,real', [
    pytest.param('boxer', 'boxer', id='exact match'),
    pytest.param('BOXER', 'boxer', id='case insensitive match'),
    pytest.param('bokser', 'boxer', id='near match'),
    pytest.param('Mastiff', 'mastiff', id='other match'),
    pytest.param('Boceron', 'boxer', id='variant'),
])
def test_can_get_best_matching_dog_breed(breedlist, given, real):
    assert DogBreedLogic(breedlist).try_get_breed(given) == real

@pytest.mark.parametrize('given,real', [
    pytest.param('aaaaxxxx', 'aaaaaaaa', id='threshold == .5'),
    pytest.param('aaaaaxxx', 'aaaaaaaa', id='threshold > .5'),
    pytest.param('aaaxxxxx', 'onbekend', id='threshold < .5 _1'),
    pytest.param('a', 'onbekend', id='threshold < .5 _2'),
])
def test_unknown_breed_type_will_be_marked_as_onbekend(given, real):
    breedlist = ['aaaaaaaa']
    assert DogBreedLogic(breedlist).try_get_breed(given) == real

def test_ambigeous_match_selects_highest_ranked_breed():
    breedlist = ['no_match', 'candidate_y', 'candidate_x']
    assert DogBreedLogic(breedlist).try_get_breed('candidaat') == 'candidate_y'



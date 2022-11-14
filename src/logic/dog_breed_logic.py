from functools import lru_cache
import Levenshtein as lev

class DogBreedLogic():
    MATCH_THRESHOLD = .5
    
    def __init__(self, breeds:list = None):
        self.breeds = breeds or ['boxer', 'mastiff', 'bouvier']
    
    def try_get_breed(self, breed_name: str):
        best_prob, best_breed = 65535, ''
        for breed in self.breeds:
            prob = self.get_similarity(breed_name, breed)
            if prob == 0:
                return breed
            if prob < best_prob:
                best_breed = breed
                best_prob = prob

        similarity_ratio = (len(breed_name) - best_prob) / len(breed_name)
        if similarity_ratio < self.MATCH_THRESHOLD:
            return 'onbekend'
            
        return best_breed
        
    @classmethod
    @lru_cache
    def get_similarity(self, name1, name2):
        name1 = name1.lower()
        name2 = name2.lower()
        return lev.distance(name1, name2)
        
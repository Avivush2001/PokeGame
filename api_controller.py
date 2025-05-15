import requests
from pokemon import Pokemon
import random
API_URL = "https://pokeapi.co/api/v2/"

# Controller class for the api
class APIController:
    def __init__(self):
        res = requests.get(API_URL + 'pokemon?limit=1')
        self.total_pokemon = res.json()['count']

    # Gets a list of random pokemon by count
    def get_pokemon(self, count):
        random_ids = random.sample(range(1, self.total_pokemon), count)
        pokemon_list = []
        for poke_id in random_ids:
            url = API_URL + "pokemon/" + str(poke_id)
            res = requests.get(url)

            if res.status_code == 200:
                data = res.json()
                pokemon_list.append(Pokemon(data['name'], data['weight'], data['height']))
            else:
                raise Exception('Error connecting to pokeapi.co')
        return pokemon_list
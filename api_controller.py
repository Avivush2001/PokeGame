import requests
from pokemon import Pokemon
import random
API_URL = "https://https://pokeapi.co/api/v2/https://pokeapi.co/+"

class APIController:
    def __init__(self):
        res = requests.get('https://pokeapi.co/api/v2/pokemon?limit=1')
        self.total_pokemon = res.json()

    def get_pokemon(self, count):
        random_ids = random.sample(range(1, self.total_pokemon + 1), count)
        pokemon_list = []
        for id in random_ids:
            url = "https://pokeapi.co/api/v2/pokemon/" + str(id)
            res = requests.get(url)
            if res.status_code == 200:
                data = res.json()
                pokemon_list.append(Pokemon(data['name'], data['weight'], data['height']))
            else:
                raise Exception('Error connecting to pokeapi.co')
        return pokemon_list
from pokemon import Pokemon
import json
import random
from api_controller import APIController

# Controller class for the data base
class DBController:
    def __init__(self):
        self.pokemon_dict = {}
        self.api_controller = APIController()
        try:
            with open("poke.json", "r") as f:
                data = json.load(f)
                for poke in data:
                    self.pokemon_dict[poke["name"]] = Pokemon(poke["name"], poke["weight"], poke["height"])
        except FileNotFoundError:
            with open("poke.json", "w") as f:
                json.dump([], f, indent=3)

    def insert_pokemon_list(self, pokemon_list):
        with open("poke.json", "r") as f:
            data = json.load(f)
        for pokemon in pokemon_list:
            if pokemon.name not in self.pokemon_dict:
                data.append(pokemon.as_dict())
                self.pokemon_dict[pokemon.name] = pokemon

        with open("poke.json", "w") as f:
            json.dump(data, f, indent=3)

    def get_random_pokemon(self):
        random_pokemon = [random.choice(self.api_controller.get_pokemon(1))]
        self.insert_pokemon_list(random_pokemon)
        return random_pokemon[0]
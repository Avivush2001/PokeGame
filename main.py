import requests
import json
from db_controller import DBController

def main():
    response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=1')
    if response.status_code == 200:
        total_pokemon = response.json()
        print("Total pokemon: " + str(total_pokemon))
        print(total_pokemon.values())
    else:
        print("Error connecting to pokeapi.co")
        return
    contr = DBController()



if __name__ == '__main__':
    main()


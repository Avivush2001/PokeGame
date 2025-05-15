import requests
import json

from api_controller import APIController
from db_controller import DBController

def main():
    db_controller = DBController()
    flag = True
    while flag:
        res = input('Would you like to draw a pokemon? (y/n): ')
        if res == 'y':
            random_pokemon = db_controller.get_random_pokemon()
            print(random_pokemon)
            print('\n')
        elif res == 'n':
            flag = False
        else:
            print("Invalid input. Please try again.")
    print('Good bye!')

def test():
    API_URL = "https://pokeapi.co/api/v2/"
    res = requests.get(API_URL + 'pokemon?limit=10')
    print (res.json())



if __name__ == '__main__':
    main()


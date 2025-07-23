#Daniel Preller, 23 July 2025, Assignment 9.2
#Program to return the list of Pokémon generations from the Pokéapi API

import requests, json

def main():
    response = requests.get('https://pokeapi.co/api/v2/generation')# The example limited it to only the first two generations, but I removed the limit to show all nine
    print(response.status_code)
    #Connection test

    print(response.json())# Unformatted results

    generations = json.dumps(response.json(), indent=4)
    print("\n" + generations)
    #Formatted results

if __name__ == '__main__':
    main()
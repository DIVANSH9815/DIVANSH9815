import requests
import json

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}pokemon/{name}"  # Fixed extra '/'
    response = requests.get(url)
    
    if response.status_code == 200:
        pokemon_data = response.json()  # Correct variable name
        return pokemon_data  # Return data instead of printing
    else:
        print(f"Error: {response.status_code}")
        return None  # Return None if request fails

# Calling the function
pokemon_name = "pikachu"
pokemon_info = get_pokemon_info(pokemon_name)  # Store the returned data

# Check if data is valid before accessing it
if pokemon_info:
    print(f"Name: {pokemon_info['name']}")
    print(f"Weight: {pokemon_info['weight']}")
    print(f"Height: {pokemon_info['height']}")
    

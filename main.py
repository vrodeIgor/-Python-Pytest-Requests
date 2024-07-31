import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'a8f537b7c9102a0f0a4abcdd3d423e30'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

body_sozdanie = {
    "name": "Бульбазавр",
    "photo_id": 1
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_sozdanie)
print(response_create.text)

pokemon_id = response_create.json()['id']
print(pokemon_id)

body_zamena = {
    "pokemon_id": pokemon_id,
    "name": "Прикол",
    "photo_id": 2
}

response_zamena = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_zamena)
print(response_zamena.text)

body_lovushka = {
    "pokemon_id": pokemon_id
}

response_lovushka = requests.put(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_lovushka)
print(body_lovushka.text)
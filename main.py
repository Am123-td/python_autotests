import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '1457845315a1a5bc8885858f49325d37'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}

body_create = {
    "name": "generate",
    "photo_id": -1
}

body_change = {
    "pokemon_id": "234265",
    "name": "Bird",
    "photo_id": 16
}

body_catch = {
    "pokemon_id": "234265"
}

response_create = requests.post (url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print (response_create.text)

message_create = response_create.json()['message']
print (message_create)

response_change = requests.put (url=f'{URL}/pokemons', headers = HEADER, json = body_change)
print (response_change.text)

message_change = response_change.json()['message']
print (message_change)

response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch)
print(response_catch.text)

message_catch = response_catch.json()['message']
print(message_catch)
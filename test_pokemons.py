import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'a8f537b7c9102a0f0a4abcdd3d423e30'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '4096'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers')
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/trainers')
    assert response_get.json()['id'] == TRAINER_ID    
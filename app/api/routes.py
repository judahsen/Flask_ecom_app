from flask import Blueprint
import requests as r

api = Blueprint('api',__name__, url_prefix='/api')

@api.get('/poke/<name_id>')
def get_poke(name_id):
    res = r.get(f"https://pokeapi.co/api/v2/pokemon/{name_id}")
    data = res.json()
    print(data)
    name = data['name']
    if data['sprites']['other']['dream_world']:
        img = data['sprites']['other']['dream_world']
    else:
        img = data['sprites']['front_shiny']
    species = data['species']['name']
    return {
        'name': name,
        'price': img,
        'description': species
    }

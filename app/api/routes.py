from flask import Blueprint
import requests as r
from ..models import User,Product

api = Blueprint('api',__name__, url_prefix='/api')

@api.get('/poke/<name_id>')
def get_poke(name_id:str):
    if name_id.isnumeric():
        poke = Product.query.get(name_id)
    else:
        poke = Product.query.filter_by(name=name_id).first() 
    if poke:
        return poke.to_dict()
    res = r.get(f"https://pokeapi.co/api/v2/pokemon/{name_id}")
    data = res.json()
    print(data)
    name = data['name']
    if data['sprites']['other']['dream_world']:
        img = data['sprites']['other']['dream_world']
    else:
        img = data['sprites']['front_shiny']
    species = data['species']['name']
    poke = Product(name,  img, species)
    poke.save_product()
    return poke.to_dict()  
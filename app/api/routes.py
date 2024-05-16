# from flask import Blueprint, request
# from ..tools import poke_getter
# from ..models import User,Product

# api = Blueprint('api',__name__, url_prefix='/api')

# @api.get('/poke/<name_id>')
# def get_poke(name_id:str):
#     if name_id.isnumeric():
#         poke = Product.query.get(name_id)
#     else:
#         poke = Product.query.filter_by(name = name_id).first() 
#     if poke:
#         return poke.to_dict()
#     try:
#         return poke_getter(name_id)
#     except:
#         return { 'error': 'try a working pokemon name or id!'}
    
# @api.post('/addteam')
# def add_team():
#     data = request.get_json()
#     print(data)
#     return {"message": "Got Your team", "data":data}
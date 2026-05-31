from flask import Blueprint, request  
from controllers.jogo_controllers import get_jogos, create_jogo, get_jogo_by_id, update_jogo,  delete_jogo

# Define um Blueprint para as rotas de "Jogo"
jogo_routes = Blueprint('jogo_routes', __name__)  

# Rota para listar todos os filmes (GET)
@jogo_routes.route('/Jogo', methods=['GET'])
def jogos_get():
    return get_jogos()

# Rota para criar um novo filme (POST)
@jogo_routes.route('/Jogo', methods=['POST'])
def jogos_post():
    return create_jogo(request.json)

@jogo_routes.route('/Jogo/<int:id>', methods=['GET'])
def jogo_get_id(id):
    return get_jogo_by_id(id)

@jogo_routes.route('/Jogo/<int:jogo_id>', methods=['PUT'])
def jogos_put(jogo_id):
    return update_jogo(jogo_id, request.json)

@jogo_routes.route('/Jogo/<int:jogo_id>', methods=['DELETE'])
def jogos_delete(jogo_id):
    return delete_jogo(jogo_id)

from itsdangerous import json
import redis    
import json
# from banco_dados_services import listar_todos_contatos_ativos
from services.banco_dados_services import listar_todos_contatos_ativos

redis_cliente = redis.Redis(host='localhost', port=6379, db=0)


def buscar_cache_contato_id(id_contato):
    todos_contatos = buscar_cache_todos_contatos()
    for contato in todos_contatos:
        if id_contato == contato['id_contato']:
            return contato
    else:
        return None


def buscar_cache_todos_contatos():
    contatos_cache = redis_cliente.get('contatos')
    if contatos_cache:
        contatos_cache_json = json.loads(contatos_cache)
        return contatos_cache_json
    else:
        return None


def atribuir_cache_todos_contatos():
    contatos_banco_dados = listar_todos_contatos_ativos()
    contatos_json_dumps = json.dumps(contatos_banco_dados)
    redis_cliente.set('contatos', contatos_json_dumps)

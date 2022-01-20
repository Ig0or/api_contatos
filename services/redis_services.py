from itsdangerous import json
import redis    
import json
from datetime import timedelta

redis_cliente = redis.Redis(host='localhost', port=6379, db=0)


def buscar_cache_todos_contatos():
    contatos_cache = redis_cliente.get('contatos')
    if contatos_cache:
        contatos_cache_json = json.loads(contatos_cache)
        return contatos_cache_json
    else:
        return None


def atribuir_cache_todos_contatos(contatos):
    contatos_json_dumps = json.dumps(contatos)
    redis_cliente.set('contatos', contatos_json_dumps)


def buscar_cache_contato_id(id_contato):
    contato_cache = redis_cliente.get(id_contato)
    if contato_cache:
        contato_cache_json = json.loads(contato_cache)
        return contato_cache_json
    else:
        return None


def atribuir_cache_contato_id(contato):
    contato_json_dumps = json.dumps(contato)
    redis_cliente.set(contato['id_contato'], contato_json_dumps)


def deletar_cache_contato_removido(id_contato):
    redis_cliente.delete(id_contato)

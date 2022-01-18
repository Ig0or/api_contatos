import re
from pymongo import MongoClient

class Conexao:
    conexao = MongoClient('mongodb+srv://igorp:abc123abc@cluster0.gtpqq.'
                        'mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
    banco_de_dados = conexao['teste']
    colecao_contatos = banco_de_dados['colecao_teste']


def inserir_contato(contato):
    Conexao.colecao_contatos.insert_one(contato)


def listar_todos_contatos_ativos():
    contatos = Conexao.colecao_contatos.find({'situacao': 'ativo'}, {'_id': 0})
    return list(contatos)


def listar_contato_por_id(id_contato):
    contato = Conexao.colecao_contatos.find_one({'id_contato': id_contato}, {'_id': 0})
    if verificar_status_contato():
        return contato
    else:
        return 


def verificar_status_contato(contato):
    if contato['situacao'] == 'ativo':
        return True
    else:
        return False

listar_contato_por_id('124e5155-4583-4539-801c-7b46f24c6411')
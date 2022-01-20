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
    contatos_lista = list(contatos)
    return contatos_lista


def listar_contato_por_id(id_contato):
    contato = Conexao.colecao_contatos.find_one({'id_contato': id_contato, 'situacao': 'ativo'}, {'_id': 0})
    return contato


def editar_contato(informacoes_novas):
    Conexao.colecao_contatos.find_one_and_update({'id_contato': informacoes_novas['id_contato']}, {'$set': informacoes_novas})


def desativar_contato(id_contato):
    return Conexao.colecao_contatos.find_one_and_update({'id_contato': id_contato, 'situacao': 'ativo'}, {'$set': {'situacao': 'inativo'}})


def buscar_contatos_por_letra(letra_buscada):
    regex_nome = {'$regex': f'^{letra_buscada}', '$options': 'i'}
    contatos = Conexao.colecao_contatos.find({'nome': regex_nome, 'situacao': 'ativo'}, {'_id': 0})
    contatos_lista = list(contatos)
    return contatos_lista

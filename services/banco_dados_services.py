from pymongo import MongoClient

class Conexao:
    conexao = MongoClient('mongodb+srv://igorp:abc123abc@cluster0.gtpqq.'
                        'mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
    banco_de_dados = conexao['teste']
    colecao_contatos = banco_de_dados['colecao_teste']


def inserir_contato(contato):
    Conexao.colecao_contatos.insert_one(contato)


def retonar_proximo_id():
    ultimo_contato = Conexao.colecao_contatos.find().limit(1).sort([('$natural', -1)])
    ultimo_contato = list(ultimo_contato)
    return ultimo_contato[0]['_id'] + 1


def listar_todos_contatos():
    contatos = Conexao.colecao_contatos.find()
    return list(contatos)
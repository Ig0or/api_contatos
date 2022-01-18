
from flask import Flask, request
from flask_restful import Resource, Api
from services import tratamento_services, banco_dados_services

app = Flask(__name__)
api = Api(app)
    

class CadastrarContato(Resource):
    def post(self):
        novo_contato_json = request.get_json()
        if tratamento_services.validar_informacoes(novo_contato_json):
            contato_tratado = tratamento_services.tratar_informacoes(novo_contato_json)
            banco_dados_services.inserir_contato(contato_tratado)
            response = 'Contato cadastrado com sucesso.', 200
            return response
        else:
            response =  'Erro ao cadastrar o contato.', 400
            return response


class ListarContatos(Resource):
    def get(post):
        todos_contatos = banco_dados_services.listar_todos_contatos_ativos()
        if todos_contatos:
            response = todos_contatos, 200
            return response
        else:
            response = 'Nenhum contato cadastrado.', 404
            return response


api.add_resource(CadastrarContato, '/cadastrar-contato')
api.add_resource(ListarContatos, '/contatos')

if __name__ == '__main__':
    app.run(debug=True)
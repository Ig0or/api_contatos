import json
from flask import Flask, request
from flask_restful import Resource, Api
from services import tratamento_services, banco_dados_services

app = Flask(__name__)
api = Api(app)
    

class CadastrarContato(Resource):
    def post(self):
        try:
            novo_contato_json = request.get_json()
            contato_validado_model = tratamento_services.validar_dados_recebidos(novo_contato_json)
            contato_tratado = tratamento_services.tratar_informacoes(contato_validado_model)
            banco_dados_services.inserir_contato(contato_tratado)
            return {}, 200
        except:
            return {}, 400


class ListarContatos(Resource):
    def get(self):
        contatos = banco_dados_services.listar_todos_contatos_ativos()
        if contatos:
            response = contatos, 200
            return response
        else:
            response = 'Nenhum contato cadastrado.', 404
            return response


class ListarContatoId(Resource):
    def get(self, id_contato):
        contato = banco_dados_services.listar_contato_por_id(id_contato)
        if contato:
            return contato, 200
        else:
            return 'Contato não existente', 404


class EditarContato(Resource):
    def put(self, id_contato):
        contato_informacoes_novas = request.get_json()
        contato_antigo = banco_dados_services.listar_contato_por_id(id_contato)



api.add_resource(ListarContatos, '/contatos')
api.add_resource(ListarContatoId, '/contato/<string:id_contato>')
api.add_resource(CadastrarContato, '/cadastrar-contato')


if __name__ == '__main__':
    app.run(debug=True)
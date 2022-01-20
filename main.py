from flask import Flask, request
from flask_restful import Resource, Api
from services import tratamento_services, banco_dados_services, redis_services

app = Flask(__name__)
api = Api(app)


class CadastrarContato(Resource):
    def post(self):
        try:
            contato_novo_json = request.get_json()
            contato_validado_model = tratamento_services.validar_dados_recebidos(contato_novo_json)
            contato_tratado = tratamento_services.adicionar_informacoes(contato_validado_model)
            banco_dados_services.inserir_contato(contato_tratado)
            redis_services.atribuir_cache_todos_contatos()
            resposta = contato_tratado, 200
            return 200
        except:
            resposta = {}, 400
            return resposta


class EditarContato(Resource):
    def put(self, id_contato):
        try:
            contato_informacoes_novas = request.get_json()
            contato_informacoes_novas_validado = tratamento_services.validar_dados_recebidos(contato_informacoes_novas)
            contato_atualizado = tratamento_services.editar_informacoes(id_contato, contato_informacoes_novas_validado)
            banco_dados_services.editar_contato(contato_atualizado)
            resposta = contato_atualizado, 200
            return resposta
        except:
            resposta = 'Erro ao editar o contato', 400
            return resposta


class ListarContatos(Resource):
    def get(self):
        contatos_cache = redis_services.buscar_cache_todos_contatos()
        if contatos_cache:
            resposta = contatos_cache, 200
        else:
            redis_services.atribuir_cache_todos_contatos()
            contatos_cache = redis_services.buscar_cache_todos_contatos()
            resposta = contatos_cache, 200
        return resposta


class ListarContatoId(Resource):
    def get(self, id_contato):
        contato_cache = redis_services.buscar_cache_contato_id(id_contato)
        if contato_cache:
            resposta = contato_cache, 200
        else:
            resposta = {}, 400
        return resposta


class RemoverContato(Resource):
    def delete(self, id_contato):
        contato_removido = banco_dados_services.desativar_contato(id_contato)
        if contato_removido:
            redis_services.deletar_cache_contato_removido(id_contato)
            resposta = 'Contato excluido.', 200
        else:
            resposta = {}, 400
        return resposta


class BuscarContato(Resource):
    def get(self, letra_buscada):
        contatos = banco_dados_services.buscar_contatos_por_letra(letra_buscada)
        resposta = contatos, 200
        return resposta


api.add_resource(ListarContatos, '/contatos')
api.add_resource(ListarContatoId, '/contato/<string:id_contato>')
api.add_resource(CadastrarContato, '/cadastrar-contato')
api.add_resource(EditarContato, '/editar-contato/<string:id_contato>')
api.add_resource(RemoverContato, '/remover-contato/<string:id_contato>')
api.add_resource(BuscarContato, '/buscar/<string:letra_buscada>')


if __name__ == '__main__':
    app.run(debug=True)
import uuid
from models import contato_models


def validar_dados_recebidos(contato_json):
  dados_validados = contato_models.ContatoModel(**contato_json)
  return dados_validados
  
  
def tratar_informacoes(contato):
    contato_tratado = {
      'id_contato': str(uuid.uuid4()),
      'nome': contato.nome,
      'telefones': [],
      'email': contato.email,
      'endereco': contato.endereco,
      'situacao': 'ativo'
    }

    for telefone in contato.telefones:
        contato_tratado['telefones'].append({'numero': telefone.numero, "tipo": telefone.tipo}) 
    return contato_tratado
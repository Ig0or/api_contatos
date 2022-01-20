import uuid
from models import contato_models


def validar_dados_recebidos(contato_json):
  dados_validados = contato_models.ContatoModel(**contato_json)
  return dados_validados
  
  
def adicionar_informacoes(contato):
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


def editar_informacoes(id_contato, informacoes_novas):
  contato_atualizado = {
    'id_contato': id_contato,
    'nome': informacoes_novas.nome,
    'telefones': [],
    'email': informacoes_novas.email,
    'endereco': informacoes_novas.endereco,
    'situacao': 'ativo'
  }

  for telefone in informacoes_novas.telefones:
    contato_atualizado['telefones'].append({'numero': telefone.numero, 'tipo': telefone.tipo})
  return contato_atualizado
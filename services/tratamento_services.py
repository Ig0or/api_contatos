import uuid
from typing import List
from pydantic import BaseModel, ValidationError


def validar_informacoes(contato) -> dict:
    chaves = verificar_chaves(contato)
    valores = verificar_valores(contato)
    if chaves and valores:
        return True
    else:
        return False


def verificar_chaves(contato):
    chaves = ['nome', 'telefones', 'email', 'endereco']
    for chave in chaves:
        if chave not in contato:
            return False
    return True


def verificar_valores(contato):
    for chave, valor in contato.items():
        if chave == 'telefones':
            for telefone in valor:
                if not 'numero' in telefone or not 'tipo' in telefone:
                    return False
        if not valor:
            return False
    return True


def tratar_informacoes(contato):
    contato_tratado = contato
    contato_tratado['id_contato'] = str(uuid.uuid4())
    contato_tratado['situacao'] = 'ativo'
    return contato_tratado

# class Telefone(BaseModel):
#     numero: str
#     tipo: str

# class Contato(BaseModel):
#     nome: str
#     telefones: List[Telefone]
#     email: str
#     endereco: str

# try:
#     a = Contato(nome='igor', telefones=[{'numero': '11999999', "tipo": 'type1'}], email='igor@mail.com', endereco= 'rua j')
#     print(a)
# except ValidationError as e:
#     print(e)



# cont = {
#     "nome": "Gabriel Silva 3",
#     "telefones": [
#         {
#             "numero": "11999999999",
#             "tipo": "type2"
#         }
#     ],
#     "email": "8", 
#     "endereco": "rua logo ali, 25"
# }
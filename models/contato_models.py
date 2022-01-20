from typing import List
from pydantic import BaseModel, validator


class TelefoneModel(BaseModel):
    numero: str
    tipo: str

    @validator('numero')
    def verificar_telefone_10chars(valor):
        if len(valor) >= 10:
            return valor
        else:
            raise ValueError

    @validator('tipo')
    def verificar_tipo_telefone(valor):
        tipos = ['residencial', 'celular', 'comercial']
        if valor in tipos:
            return valor
        else:
            raise ValueError


class ContatoModel(BaseModel):
    nome: str
    telefones: List[TelefoneModel]
    email: str
    endereco: str

    @validator('*')
    def verificar_valor_vazio(valor):
        if valor:
            return valor
        else:
            raise ValueError

    @validator('email')
    def verificar_arroba_email(valor):
        if '@' in valor:
            return valor
        else:
            raise ValueError


try:
    dict = {
    "nome": "felipe",
    "telefones": [
        {
        "numero": "11233322321311",
        "tipo": "residencial"
        }
    ],
    "email": "igort@",
    "endereco": "rua jose"
    }

    ContatoModel(**dict)
except Exception as e:
    print(e)
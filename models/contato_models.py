from typing import List
from pydantic import BaseModel, validator

class TelefoneModel(BaseModel):
    numero: str
    tipo: str


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

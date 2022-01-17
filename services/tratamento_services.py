from services import banco_dados_services


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
        if chave not in contato['dados']:
            return False
    return True


def verificar_valores(contato):
    for chave, valor in contato['dados'].items():
        if chave == 'telefones':
            for telefone in valor:
                if not 'numero' in telefone or not 'tipo' in telefone:
                    return False
        if not valor:
            return False
    return True


def tratar_informacoes(contato):
    ultimo_id_cadastrado = banco_dados_services.retonar_proximo_id()
    contato_tratado = contato
    contato_tratado['_id'] = ultimo_id_cadastrado
    contato_tratado['dados']['situacao'] = 'on'
    return contato_tratado
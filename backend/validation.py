'''
    MODULO DE VALIDAÇÃO DE ENTRADAS
'''
def validarAcentuacao(letra_digitada):
    letras_proibidas = ['ã', 'á', 'à', 'â', 'í', 'ì', 'î',
                        'é', 'è', 'ê', 'ç', 'ó', 'ô', 'õ', 'ò']
    for letra in letra_digitada:
        if letra in letras_proibidas:
            return False
    return True


def validacaoEntrada(letra_digitada, letras_digitadas):
    validacao = letra_digitada.isalpha()
    if (validacao == False) and (' ' not in letra_digitada):
        print('Digite alguma letra válida')
        return False
    validacao = validarAcentuacao(letra_digitada)
    if validacao == False:
        print('Digite letras sem acentuação')
        return False
    if letra_digitada in letras_digitadas:
        if len(letra_digitada) > 1:
            print('Você já digitou essa palavra!')
        else:
            print('Você já digitou essa letra!')
        return False
    else:
        return True
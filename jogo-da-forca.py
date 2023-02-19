from random import randint


def validarAcentuacao(letra_digitada):
    letras_proibidas = ['ã', 'á', 'à', 'â', 'í', 'ì', 'î',
                        'é', 'è', 'ê', 'ç', 'ó', 'ô', 'õ', 'ò']
    for letra in letra_digitada:
        if letra in letras_proibidas:
            return False
    return True


def validacaoEntrada(letra_digitada, letras_digitadas):
    validacao = letra_digitada.isalpha()
    if validacao == False:
        print('Desculpa, mas não aceitamos esse tipo caracteres')
        return False
    validacao = validarAcentuacao(letra_digitada)
    if validacao == False:
        print('Desculpa, mas não aceitamos esse tipo caracteres')
        return False
    if letra_digitada in letras_digitadas:
        if len(letra_digitada) > 1:
            print('Você já digitou essa palavra!')
        else:
            print('Você já digitou essa letra!')
        return False
    else:
        return True


file = open('palavras.txt')
palavras = file.readlines()
dados = palavras[randint(1, len(palavras))]

dados = dados.split(';')
palavra = dados[0]
dica = dados[1]
palavra_misteriosa = []  # Os tracinho que vai mostrar para o usuario
letras_da_palavra = []  # Todas as letras da palavra, acertou a letra, ela é removida
letras_digitadas = []  # Input do usuário
tamanho_tabulacao = len(dica)  # Tabulação das linhas e etc.
vida = 6
acertos = ''  # Palavras acertadas

print('Por favor, não digite palavras com acento, ou caraceter especial.')

for letra in palavra:
    palavra_misteriosa.append('_')
    letras_da_palavra.append(letra)

while (acertos != palavra) and (vida > 0):

    print(' ')
    print('-' * tamanho_tabulacao)
    print(f'{"JOGO DA FORCA":^{tamanho_tabulacao}}')
    print('-' * tamanho_tabulacao)
    print(f'Dica: {dica}')

    for tracinho in palavra_misteriosa:
        print(tracinho, end=' ')
    print()

    print('Vida: ', vida)

    letras_digitadas = list(set(letras_digitadas))

    if len(letras_digitadas) != 0:
        print('Letras digitadas:', end=' ')
        for letra in letras_digitadas:
            print(letra, end=' ')
        print()
        print('-' * tamanho_tabulacao)
        print(' ')

    letra_digitada = str(input('Digite uma letra: ')).strip().lower()

    while validacaoEntrada(letra_digitada, letras_digitadas) == False:
        letra_digitada = str(input('Digite uma letra: ')).strip().lower()

    if letra_digitada == palavra:
        break
    elif letra_digitada not in letras_da_palavra:
        print('Você errou!')
        print()
        vida -= 1

    while letra_digitada in letras_da_palavra:
        palavra_misteriosa[letras_da_palavra.index(
            letra_digitada)] = letra_digitada
        letras_da_palavra[letras_da_palavra.index(letra_digitada)] = '-'
        acertos = ''.join(palavra_misteriosa)

    letras_digitadas.append(letra_digitada)

# Para que apresente a palavra no final
if letra_digitada == palavra:
    palavra_misteriosa = palavra

# Apresenta a palavra para o jogador
for tracinho in palavra_misteriosa:
    print(tracinho, end=' ')
print()

if (acertos == palavra) or (letra_digitada == palavra):
    print('Parabéns, você venceu!')
else:
    print('Você perdeu :(')
    print(f'A palavra era: {palavra}')

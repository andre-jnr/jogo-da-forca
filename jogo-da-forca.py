from random import randint


def validacaoEntrada(tentativa, proibidas, letras_digitadas):
    while tentativa in letras_digitadas:
        print('Você já digitou essa palavra!')
        tentativa = str(input('Digite uma letra: '))
    while (tentativa in proibidas) or (tentativa.isnumeric()):
        print('Desculpa, mas não aceitamos esse tipo caracteres')
        tentativa = str(input('Digite uma letra: '))
    return tentativa


file = open('palavras.txt')
palavras = file.readlines()
dados = palavras[randint(0, len(palavras))]

letras_proibidas = ['ã', 'á', 'à', 'â', 'ã', 'í', 'ì', 'î', 'é', 'è', 'ê', 'ç']
dados = dados.split(';')
palavra = dados[0]
dica = dados[1]
palavra_misteriosa = []
letras_da_palavra = []
letras_digitadas = []
tamanho_tabulacao = len(dica)
vida = 6
acertos = ''

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

    tentativa = str(input('Digite uma letra: ')).strip().lower()
    validacao = validacaoEntrada(tentativa, letras_proibidas, letras_digitadas)
    tentativa = validacao

    if tentativa == palavra:
        break
    elif tentativa not in letras_da_palavra:
        print('Você errou!')
        print()
        vida -= 1

    while tentativa in letras_da_palavra:
        palavra_misteriosa[letras_da_palavra.index(tentativa)] = tentativa
        letras_da_palavra[letras_da_palavra.index(tentativa)] = '-'
        acertos = ''.join(palavra_misteriosa)

    letras_digitadas.append(tentativa)

if tentativa == palavra:
    palavra_misteriosa = palavra

for tracinho in palavra_misteriosa:
    print(tracinho, end=' ')
print()

if (acertos == palavra) or (tentativa == palavra):
    print('Parabéns, você venceu!')
else:
    print('Você perdeu :(')
    print(f'A palavra era: {palavra}')

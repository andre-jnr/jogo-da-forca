from backend import data as dt
from backend import frontend as front
from backend import validation as val
import os


def jogar():
    dados = dt.coletarDados('palavras.txt')
    palavra = dados[0].strip()
    dica = dados[1].strip()
    palavra_misteriosa = dt.criarPalavraMisteriosa(palavra)
    letras_para_acertar = list(palavra)
    letras_digitadas = list()
    tamanho_tabulacao = len(dica)
    vida = 6

    print('Por favor, não digite palavras com acento ou caracteres especiais.')

    while (''.join(palavra_misteriosa) != palavra) and (vida > 0):
        front.limparTerminal()
        front.cabecalho(tamanho_tabulacao, dica)

        front.exibirLetrasAcertadas(palavra_misteriosa)
        print('Vida:', vida)
        front.mostrarLetrasDigitadas(letras_digitadas, tamanho_tabulacao)

        letra_digitada = input('Digite uma letra: ').strip().lower()

        while not val.validacaoEntrada(letra_digitada, letras_digitadas):
            letra_digitada = input('Digite uma letra: ').strip().lower()

        if letra_digitada == palavra:
            break
        elif letra_digitada not in letras_para_acertar:
            print('Errou!')
            os.system("pause")
            vida -= 1

        front.substituindoTracosPorLetras(letra_digitada, letras_para_acertar, palavra_misteriosa)
        letras_digitadas.append(letra_digitada)

    if ''.join(palavra_misteriosa) == palavra:
        palavra_misteriosa = list(palavra)

    for letra in palavra:
        print(letra, end=' ')
    print()

    if (''.join(palavra_misteriosa) == palavra) or (letra_digitada == palavra):
        print('Parabéns, você venceu!')
    else:
        print('Você perdeu :(')
        print(f'A palavra era: {palavra}')


if __name__ == "__main__":
    jogar()
'''
    MODULO QUE TRATA A VISUALIZAÇÃO DE DADOS
    PARA O USUÁRIO
'''
import os

def exibirLetrasAcertadas(palavra):
    for tracinho in palavra:
        print(tracinho, end=' ')
    print()


def mostrarLetrasDigitadas(letras_digitadas, tamanho_tabulacao):
    if len(letras_digitadas) != 0:
        print('Letras digitadas:', end=' ')
        for letra in letras_digitadas:
            print(letra, end=' ')
        print()
        print('-' * tamanho_tabulacao)
        print(' ')
        return True
    else:
        return False
    

def cabecalho(tamanho_tabulacao, dica):
    print('-' * tamanho_tabulacao)
    print(f'{"JOGO DA FORCA":^{tamanho_tabulacao}}')
    print('-' * tamanho_tabulacao)
    print(f'Dica: {dica}')


def limparTerminal():
    os_name = os.name
    if os_name == "posix":
        os.system("clear")
    elif os_name == "nt":
        os.system("cls")


def substituindoTracosPorLetras(letra_digitada, letras_para_acertar, palavra_misteriosa):
    if letra_digitada in letras_para_acertar:
        while letra_digitada in letras_para_acertar:
            index = letras_para_acertar.index(letra_digitada)
            palavra_misteriosa[index] = letra_digitada
            letras_para_acertar[index] = '-'
'''
    MODULO DE MANIPULAÇÃO DE DADOS
'''
from random import randint
import os


def coletarDados(nome_arquivo):
    file = open(nome_arquivo)
    palavras = file.readlines()
    dados = palavras[randint(0, len(palavras) - 1)].split(';')
    return dados


def criarPalavraMisteriosa(palavra):
    palavra_misteriosa = list()
    for letra in palavra:
        simbolo = ' ' if letra == ' ' else '_'
        palavra_misteriosa.append(simbolo)
    return palavra_misteriosa
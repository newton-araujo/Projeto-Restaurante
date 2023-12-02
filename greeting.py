"""Aqui vamos ter uma função para dar boas vindas ao cliente"""

from datetime import datetime
from linha import linha
from time import sleep


def greeting(nome, mesa=0):
    hora = datetime.now().hour
    if hora >= 6 and hora < 12:
        hora ='BOM DIA'
    elif hora >= 12 and hora < 18:
        hora = 'BOA TARDE'
    elif hora >= 18 and hora < 24:
        hora = 'BOA NOITE'
    linha()
    print(f'{hora} Srº(a) {nome}'.center(80))
    linha()
    print(f"BEM VINDO(A) AO NOSSO RESTAURANTE".center(80))
    linha()
    sleep(1)
    linha()
    print(f"Sua mesa para {mesa} pessoas ainda não está preparada.".center(80))
    linha()
    sleep(1)
    linha()
    print(f"Srº(a) {nome} sua mesa está pronta".center(80))


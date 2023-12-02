#Vamos instância uma função para que um dos nosso atendentes realize o atendimento do cliente.
from random import choice
from linha import linha
from time import sleep

def garçom(nome):
    atendentes = ['Carlos', 'Francisco', 'João', 'Bento']
    atendente = choice(atendentes)
    
    sleep(1)
    linha()
    print(f"Olá Srº(a) {nome}, meu nome é {atendente} e vou realizar o seu atendimento.".center(80))
    linha()
    print("Esse aqui é o nossas opções".center(80))
    linha()
    print('[Carnes] - [Peixes] - [Aves] - [Saladas] - [Bebidas]'.center(80))
    linha()
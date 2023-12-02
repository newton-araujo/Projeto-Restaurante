""" 
O projeto 'Restaurante Prazeres' é um simulador de um restaurante virtual, que visa mostrar a rotina de um restaurante. Tem o intuito 
de demonstrar o conhecimento adquirido em Python até o momento.

"""    
from datetime import datetime
from time import sleep
from linha import linha
from greeting import greeting
from atendente import garçom
from cardapio import menu
from pular import pular
from pedidos import Pedido

#Lista de conta, essa lista irá armazenar todos os valores de pedido do cliente.
conta = []
comanda = []
#Entrada do cliente, e a mesa vai ser para quantas pessoas.
cliente = input('Infome o nome do cliente: ').capitalize()
mesa_para = int(input('Mesa para quantas pessoas? '))
greeting(cliente,mesa_para)
garçom(cliente)

"""
    Nessa etapa, o cliente escolherá o cardápio que deseja visualizar antes de fazer o 
    pedido. Caso não goste de nenhuma opção, poderá sair do restaurante.

"""
cardapio = ''
while cardapio != "Sair":
    linha()
    print('Deseja pedir, se sim digite "Pedir" - Se não "Sair".'.center(80))
    linha()
    pular()
    print('''
                Para acessar um dos nossos cardápios basta digitar
                o nome ou "Pedir", para que o garçom realize o seu pedido.
                     ''')
    pular()
    linha()
    cardapio = input('O que deseja fazer? ').capitalize()
    linha()
    pular()
    if cardapio == "Carnes":
        sleep(1)
        menu.carne()
    elif cardapio == "Peixes":
        sleep(1)
        menu.peixe()
    elif cardapio == "Aves":
        sleep(1)
        menu.aves()
    elif cardapio == "Saladas":
        sleep(1)
        menu.salada()
    elif cardapio == "Bebidas":
        sleep(1)
        menu.bebidas()
    elif cardapio == "Pedir":
         prato = ''
         while prato != "Enviar":
             linha()
             print('\nPodemos enviar o seu pedido, se sim digite "Enviar"\n.'.center(80))
             linha()
             prato = input('Qual o nome do prato: ').capitalize()
             if prato == 'Enviar':
                linha()
                print('Pedido realizado com sucesso!'.center(80))
                linha()
                sleep(1)
                linha()
                print('Seu pedido está sendo preparado!'.center(80))
                linha()
                sleep(1)
                linha()
                print('Seu prato está pronto. Bom apetite!'.center(80))
                linha()
                break
             
             
             quantidade = int(input('Quantos pratos vão ser: '))
             valor = float(input('Qual o valor: '))
             pedido = Pedido(prato,quantidade,valor)
             informações_do_pedido = f'{prato:<30} {quantidade:>2}UN R${valor*quantidade:.2f}'
             comanda.append(informações_do_pedido)
             conta.append(valor*quantidade)
                      
    elif cardapio == "Conta":
        linha()
        for item in comanda:
            print(item)
        saldo = sum(conta)
        print(f'Saldo -----------------------------------     R${saldo:.2f}')
            
    if cardapio == "Sair":
        sleep(1)
        linha()
        print(f'''
                Espero que você tenha tido uma experiência maravilhosa e 
                que os nossos pratos tenham proporcionado grande alegria e prazer.
                '''.center(100))
        linha()
        break
    

print('Obrigado pela visita.'.center(80))
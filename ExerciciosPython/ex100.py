# Faça um programa que tenha uma lista chamada números e duas funções chamadas sortear() e soma_Par().
# A primeira função vai sortear 5 números e vai colocá-los dento de uma lista e a segunda função vai mostrar a soma entre os valores para sorteados pela função anterior.

from random import randint
from time import sleep


def sortear(sorteio):
    print(f'Sorteando 5 valores da lista: ', end='')
    for valor in sorteio:
        print(f'{valor}', end=' ', flush=True)
        sleep(0.3)
        numeros.append(valor)
    print('PRONTO!!')


def soma_Par():
    total = 0
    print(f'Somando os valores pares de {numeros}, temos', end=' ')
    for valor in numeros:
        if valor % 2 == 0:
            total += valor
    print(f'{total}')
numeros = []

#programa principal
sortear([randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(1, 10)])
soma_Par()

"""
from random import randint
from time import sleep

def sorteia(lista):
    print('Sorteando 5 valores da lista', end=' ')
    for con in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n}', end=' ', flush=True)
        sleep(0.4)
    print('PRONTO!')

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')

numeros = []
sorteia(numeros)
somaPar(numeros)

"""

'''
Ex: 2
from random import randint
from time import sleep
sorteio = []


def sortear():
    """
    -> Função faz o sortear 5 números aleatórios utilizando a bíblioteca random
    :return: Sem return
    """
    print(f'Sorteando 5 valores: ', end='')
    while len(sorteio) < 5:
        num = (int(randint(0, 10,)))
        if num not in sorteio:
            sorteio.append(num)
    for v in sorteio:
        sleep(0.3)
        print(v, end=' ', flush=True)
    print('PRONTO)!! ')


def soma_Par(lis):
    """
    -> Função faz a separação dos números pares e a soma posterior deles.
    :param lis: É a lista sorteio [] gerada na função sortear.
    :return: Sem return
    """
    total = 0
    for c in lis:
        if c % 2 == 0:
            total += c
    print(f'Somando os valores pares de {sorteio}, temos {total}')


def continuar():
    """
    -> Função foi feita para criar um loop e só parar quando dizer não.
    :return: Sem retorn
    """
    while True:
        sortear()
        soma_Par(sorteio)
        while True:
            continuar = str(input('Quer continuar? [N/S]: ')).strip().upper()[0]
            if continuar in 'NS':
                sorteio.clear()
                break
            print('Opção invalida!! Digite somente S ou N.')
        if continuar == 'N':
            break
    sleep(1)
    print('FIM.. Obrigado por participar')


# Programa Principal
continuar()


'''
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
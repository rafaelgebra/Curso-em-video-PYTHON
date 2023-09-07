from random import randint
from time import sleep

def sortear(sorteio):
    print(f'Sorteando 5 valores da lista: ', end='')
    for valor in sorteio:
        print(f'{valor}', end=' ', flush=True)
        sleep(0.3)
    print('PRONTO!!')
def soma_Par():
    print(f'Somando os valores pares de {sortear}')




#programa principal
sortear([randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(1, 10)])
soma_Par()
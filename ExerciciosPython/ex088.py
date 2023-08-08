from random import randint
from time import sleep
lista = []
jogos = []
print('-'*40)
print(f'{"JOGA NA MEGA SENA":^40}')
print('-'*40)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont +=1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot +=1 
for i , l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print(f'{" < BOA SORTE! > ":-^40}')



"""

from time import sleep
from random import randint
print('-'*40)
print(f'{"JOGANDO NA MEGA SENA":^40}')
print('-'*40)
num = int(input('Quantos jogos você quer que eu sorteie? '))
for c in range(1, num+1):
    sorteio = [[randint(0, 60,)],[randint(0, 60,)],[randint(0, 60,)],[randint(0, 60,)],[randint(0, 60,)],[randint(0, 60,)]]
    print(f'Jogo {c:>2}: {sorteio}')
    sleep(1)
print(f'{"BOA SORTE":-^40}')

from random import randint
from time import sleep
lista_Temp = []
lista_Final = []
print('-'*50)
print(f'{"JOGA NA MEGA SENA":^50}')
print('-'*50)
quant = int(input('Quando jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista_Temp:
            lista_Temp.append(num)
            cont += 1
        if cont >= 6:
            break
    lista_Temp.sort()
    lista_Final.append(lista_Temp[:])
    lista_Temp.clear()
    tot += 1
print('-='*3, f'SORTEANDO {quant} JOGOS', '-='*3 )
for i, lista in enumerate(lista_Final):
    sleep(1)
    print(f'Jogo {i+1}: {lista}')
sleep(1)


EX: 2

from random import randint
from time import sleep
lista_Temp = []
lista_Final = []
quant = int(input('Quando jogos você quer eu eu faça? '))
total = 1
while total <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista_Temp:
            lista_Temp.append(num)
            cont += 1    
        if cont >= 6:
            break
    lista_Temp.sort()
    lista_Final.append(lista_Temp[:])
    lista_Temp.clear()
    total += 1
for pos, lista in enumerate(lista_Final): 
    sleep(1)    
    print(f'O jogo {pos+1}º: {lista}')
sleep(1)


"""
from random import randint
numeros = (randint(0, 10), randint(0, 10), randint(0, 10),
             randint(0, 10), randint(0, 10), )
print(f'Os valores sorteados foram {numeros}')
print(f'O maior numero é {max(numeros)}')
print(f'O menor numero é {min(numeros)}')



"""
from random import randint
sorteio = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10) )
c = maior = menor = 0#Sem a função max()e min()

print(f'Os numeros sorteados foram', end=' ')
for elemento in sorteio:
    c += 1#Sem a função max()e min()
    print(f'{elemento}', end=' ')
    if c == 1: #Sem a função max()e min()
        menor = menor = elemento
    else:
        if elemento < menor:
            menor =  elemento
        elif elemento > maior:
            maior = elemento

print(f'\nO MAIOR valor é {max(sorteio)}.... usando a função max(sorteio)')
print(f'O menor valor é {min(sorteio)}.... usanda a função min(sorteio)')


print(f'O MAIOR é {maior}.... SEM a função max() \nO menor é {menor}.... SEM a função min()') #usando a opção de maior e igual em tupla

"""
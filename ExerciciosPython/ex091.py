from random import randint
from time import sleep
from operator import itemgetter
jogos = {}
"""jogos = {'jogador1': randint(1, 6),
           'jogador2': randint(1, 6),
           'jogador3': randint(1, 6),
           'jogador4': randint(1, 6),} #dentro do Dicionario é colocado assim."""
ranking = {}
for num in range(0, 4):
    jogos[f'jogador{num+1}'] = randint(1, 6) # fora do dicionario é colocado assim.

for keys, values in jogos.items():
    sleep(1)
    print(f'{keys} tirou {values} no dado')
print('='*40)
print(f'{"  == RANKING DOS JOGADORES ==  ":^40}')
cont = 1
ranking = sorted(jogos.items(), key=itemgetter(1), reverse=True) #para usar a FUNÇÃO itemgetter, tem que fazer a importação depois pode usa-lo para ordenar por posição 'parte' nesse caso foi celecionado a (parte 1) que é o valor, a função reverse=True foi usado para inverter do maior pra o menor.
for cont, values in enumerate(ranking): 
    print(f'{cont+1}º lugar: {values[0]} com {values[1]}')
import random
from time import sleep # Essa função faz con que demore algum tempo para continuar a leitura da linha de comando
com = random.randint(0, 5) # "PENSAR" na realidade esta sorteando o número aleatório.
print('-=-'*30)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*30)

num = int(input('Em que número eu pensei? '))
print('Processando...')
sleep(2) # o conteudo dentro do () é os segundos de espera
if num >= 0 and num <= 5:
    if num == com:
        print('Parabéns você acertou!!')
    else:
        print('Você errou, tente novamente!!')
elif num >= 6:
        print('Número invalido!!')
        print('Tente novamente!!')


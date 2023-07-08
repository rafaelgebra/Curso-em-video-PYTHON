from random import randint
computador = randint(0, 10)
print('Sou o seu computador... Acabei de pensar em um numero entre 0 a 10 ')
print('Sera que voce consegui descobrir? ')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual e o seu palpite? '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez')
print('Acertou com {} tentativas. Parabens!'.format(palpite))

"""
from random import randint
from time import sleep
computador = randint(0,10)
print(computador)
print('Sou o seu computador...')
sleep(1)
print('Acabei de pensar em um número entre 0 e 10.')
sleep(1)
print('Será que você consegue adivinhar qual é?')
sleep(1)
pessoa = int(input('Qual o seu palpite?. '))
tentativas = 0
while computador != pessoa :
    tentativas += 1
    if pessoa > computador:
        print('Menos ... Tente outra vez.')
        sleep(1)
    if pessoa < computador:
        print('Mais... Tente mais uma vez ')
        sleep(1)     
    pessoa = int(input('Qual o seu palpite?. '))
print('Acertou com {} tentativas. Parabéns!! ' .format(tentativas))
"""

from random import randint
from time import sleep
computador = randint(0,10)
print(computador)
print('Sou o seu computador...')
sleep(0.1)
print('Acabei de pensar em um número entre 0 e 10.')
sleep(0.2)
print('Será que você consegue adivinhar qual é?')
sleep(0.2)
pessoa = int(input('Qual o seu palpite? '))
c = 0

while computador != pessoa :

    for c in range(1, 11):
        if c < 10:
            c += 1     
            pessoa = int(input('ERRO! Essa foi a tentativa de número {} ' .format(c)))
        else:
            pessoa = computador
    print('Acabou as suas chances. Tente mais tarde!!')
print('Parabéns você acertou!!')

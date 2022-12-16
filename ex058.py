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

from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Suas opcoes:
[0] PEDRA
[1] PAPEL
[2] TESOURA ''')
jogador = int(input('Qual e a sua jogada '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-=' * 11)
print('Computado jogou {}'. format(itens[computador]))
print('Jogador jogou {}' .format(itens[jogador]))
print('-=' *20)
if computador == 0: #PEDRA#
    if jogador == 0: #PEDRA#
        print('EMPATE')
    elif jogador == 1: #PAPEL#
        print('JOGADOR VENCE')
    elif jogador == 2: #TESOURA#
        print('COMPUTADOR VENCEU')
    else:
        print('JOGADA INVALIDA!!')
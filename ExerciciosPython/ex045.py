from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
#print('{}' .format(itens[computador]))
print('''Suas opcoes:
[0] PEDRA
[1] PAPEL
[2] TESOURA ''')
jogador = int(input('Qual e a sua jogada? '))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')
sleep(0.5)
print('-=' * 11)
print('Computado jogou {}'. format(itens[computador]))
print('Jogador jogou {}' .format(itens[jogador]))
print('-=' *20)
if computador == 0: #Computador jogou PEDRA
    if jogador == 0: #PEDRA
        print('EMPATE')
    elif jogador == 1: #PAPEL
        print('JOGADOR VENCE')
    elif jogador == 2: #TESOURA
        print('COMPUTADOR VENCEU')
    else:
        print('JOGADA INVALIDA!!')
elif computador == 1: #Computador jogou PAPEL
    if jogador == 1: #PAPEL
        print('EMPATE')
    elif jogador == 0:#PEDRA
        print('COMPUTADOR VENCEU')
    elif jogador == 2: #TESOURA
        print('JOGADOR VENDEU')
    else:
        print('JOGADA INVALIDA!!')
elif computador == 2: #Computador jogou TESOURA
    if jogador == 2: #TESOURA
        print('EMPATE')
    elif jogador == 0: #PEDRA
        print('JOGADOR VENDEU')
    elif jogador == 1: #PAPEL
        print('COMPUTADOR VENDEU')
    else:
        print('JOGADA INVALIDA!!')

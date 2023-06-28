#'''faça um programa que mostre na tela #
#uma contagem regressiva para o estouro de fogos de artificio,#
#indo de 10 ate 0, com uma pausa de 1 segundo entre eles.'''#
from time import sleep
# o inicio tem que ser MAIOR que o fim #
i = int(input('Inicio '))
f = int(input('Fim '))
for c in range(i, f-1, -1):
    print(c)
    sleep(1)
print('BUM! BUM!' + '\U0001F386')

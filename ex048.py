# Faca um programa que colcule a soma entre totos os numeros #
# impares que sao multiplos de tres e que se encontram no #
# intervalo de 1 ate 500 #
from time import sleep
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        soma += c
        print(c, end=' ')
        sleep(0.01)
print('Soma de {} numeros que sao divisiveis por 3 e {} '.format(cont, soma,))
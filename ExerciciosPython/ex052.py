# Faca um programa que leia um numero inteiro #
# e diga se ele e ou nao um numero PRIMO #
num = int(input('Digite um numero inteiro '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\33[33m', end='')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO numero {} e foi dividido {} vezes'.format(num, tot))
if tot == 2:
    print('O numero {} e e primo'.format(num))


"""
print('='*30)
print('{:^30}'.format(' SERÁ QUE É NÚMERO PRIMO? '))
print('='*30)
num = int(input('Digite um número: '))
primos = 0
for c in range(1, num +1):
    if num % c == 0:
        print('\033[33m', end=' ')
        primos += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
if primos == 2:
    print('\n\033[mO número {} é primo porque foi dividido {} vezes.' .format(num, primos))
else:
    print('\n\033[mO número {} não é primo porque foi dividido {} vezes.' .format(num, primos))
"""
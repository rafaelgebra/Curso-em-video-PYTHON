# Faca um programa que leia um numero inteiro #
# e dica se ele e ou nao um numero PRIMO #
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
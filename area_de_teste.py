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
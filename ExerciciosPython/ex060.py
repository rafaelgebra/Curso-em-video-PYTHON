n = int(input('Digite um numero para calcular o seu fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
for c in range(n, 0, -1):
    f *= c
    c -= 1
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
print('{}'.format(f))


"""
num = int(input('Digite um número: '))
c = num
f = 1
print('Calculando {}! = ' .format(num), end=' ')
while c > 0:
    print('{} '.format(c), end='')
    print(' x ' if c > 1 else '= ', end='')
    f *= c
    c -= 1
print('{}' .format(f))
    
    
"""


"""
from math import factorial
num = int(input('Digite um número para calcular seu Fatorial: '))
f = factorial(num)
print('O fatorial de {} é {}' .format(num, f))
"""

# Refaça o desafio 009, mostrando a #
# tabuada de um número que o usuario escolher, #
# só que agora ultilizando um laço for #
'''
             # Exercicio 009 #

n1 = int(input('Digite um numero '))
print('-' * 12)
print('{} x {:2} = {:2}'.format(n1, 1, (n1*1)))
print('{} x {:2} = {:2}'.format(n1, 2, (n1*2)))
print('{} x {:2} = {:2}'.format(n1, 3, (n1*3)))
print('{} x {:2} = {:2}'.format(n1, 4, (n1*4)))
print('{} x {:2} = {:2}'.format(n1, 5, (n1*5)))
print('{} x {:2} = {:2}'.format(n1, 6, (n1*6)))
print('{} x {:2} = {:2}'.format(n1, 7, (n1*7)))
print('{} x {:2} = {:2}'.format(n1, 8, (n1*8)))
print('{} x {:2} = {:2}'.format(n1, 9, (n1*9)))
print('{} x {:2} = {:2}'.format(n1, 10, (n1*10)))
print('-'* 12) '''

n = int(input('Digite um numero inteiro. '))
for c in range(1, 11):
    print('{} x {} = {}'.format(n, c, (n*c)))

"""
num = int(input('Digite um número para ver a tabuada '))
for n in range(0, 11):
    tab = num * n
    print('{} x {:>2} = {:>2}' .format(num, n, tab))
"""
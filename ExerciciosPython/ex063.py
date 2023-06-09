"""Escreva um programa que leia um numero N inteiro
qualquer e mostre na tela os N primeiros elementos
de uma Sequencia de Fibonacci."""

print('-'*25)
print('Sequencia de Fibonacci')
print('-'*25)
n = int(input('Quantos termos voce quer mostrar? '))
t1 = 0
t2 = 1
cont = 0
print('{}-> {}'.format(t1, t2), end='-> ')
while cont <= n:
    cont += 1
    t3 = t1 +t2
    print('{}'.format(t3), end='-> ')
    t1 = t2
    t2 = t3
print('Fim')

'''n = int(input('Quantos termos voce quer mostrar? '))
t1 = 0
t2 = 1
cont = 3
print('{}-> {}'.format(t1, t2), end=' ')
while cont <= n:
    cont += 1
    t3 = t1 + t2
    print('-> {}'.format(t3), end=' ')
    t1 = t2
    t2 = t3
print("fim")
'''

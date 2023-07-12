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

"""
print('-'*30)
print('{:^30}'.format('SEGUÊNCIA DE FIBONACCI'))
print('-'*30)
num = int(input('Quantos termos você quer mostar: '))
termo1 = 0
termo2 = 1
cont = 3
print('='*30)
print('{} -> {} -> '.format(termo1,termo2), end=' ')
while cont <= num:
    cont += 1
    termo3 = termo1 + termo2
    print('{} -> '.format(termo3), end=' ')
    termo1 = termo2
    termo2 = termo3
print('FIM')
print('='*30)

"""
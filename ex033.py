print('Digite uma seguencia de 3 numeros:')
n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo numero: '))
n3 = float(input('Digite o terceiro numero: '))
# Esta correto.
"""if n1 > n2 and n1 > n3:
    print('O primeiro numero e o maior numero {}'.format(n1))
if n2 > n3 and n2 > n1:
    print('O segundo numero e o maior numero {}'.format(n2))
if n3 > n1 and n3 > n2:
    print('O terceiro numero e o maior numero {}'.format(n3))
if n1 < n2 and n1 < n3:
    print('O primeiro numero e o menor numero {}'.format(n1))
if n2 < n3 and n2 < n1:
    print('O segundo numero e o menor numero {}'. format(n2))
if n3 < n1 and n3 < n2:
    print('O terceiro numero e o menor numero {}'.format(n3))"""
#Verificando o MENOR valor
menor = n1
if n2 < n3 and n2 < n1:
    menor =  n2
if n3 < n1 and n3 < n2:
    menor = n3
#verificando o MAIOR valor
maior = n1
if n2 > n3 and n2 > n1:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O menor valor digitado foi {}{}{}'.format('\033[31m', menor, '\033[m'))
print('O maior valor digitado foi {}{}{}'.format('\033[32m', maior, '\033[m'))

tabela = (int(input('Digite um número: ')),
     int(input('Digite um número: ')),
      int(input('Digite um número: ')),
       int(input('Digite um número: ')))
# A topla a baixo não esta errada porém pode ser feita de outra forma
# n1 = int(input('Digite um número: '))
# n2 = int(input('Digite outro número: '))
# n3 = int(input('Digite mais um número: '))
# n4 = int(input('Digite o últimoa número: '))
# tabela = (n1, n2, n3, n4)
print(f'Você digitou os valores{tabela}')
print(f'O valor 9 aparece {tabela.count(9)} vezes') # O count mostra quantas vezez aparece o numero/letra selecionado
if 3 in tabela:
    print(f'O valor 3 apareceu pela primeira vez na posição {tabela.index(3)}') # na responta sempre mais mostrar uma posição a menos, isso acontece porque a tupla começa na posição 0 ZERO, caso queira deixar um uma posição mais parecida com o que esta aparecendo só somar +1 depois da aspas.
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print(f'Os numeros pares são', end=' ')
for n in tabela:
    if n % 2 == 0:
        print(n, end=', ')


"""
'''
    pode ser feito assim também

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite mais um número: '))
num4 =  int(input(('Digite o último número: ')))
tupla = (num1, num2, num3, num4)
'''
tupla = ((int(input('Digite um número: '))), (int(input('Digite outro número: '))),
         (int(input('Digite mais um número: '))), (int(input(('Digite o último número: ')))))

print(f'Você digitou os valores {tupla}')
print(f'O valor 9 apareceu {(tupla.count(9))} vezes')
if 3 in tupla:
    print(f'O valor 3 apareceu na {tupla.index(3)+1} posição')
else:
    print('Não tem o número 3 digitado na atual tupla ')
print('O valores pares digitados foram ', end=' ')
for elemento in tupla:
    if elemento % 2 == 0:
        print((elemento),end=', ')

"""
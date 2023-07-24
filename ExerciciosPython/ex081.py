lista = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    r = str(input('Você quer continuar? [S/N]')).upper()[0]
    if r in 'Nn':
        break
if 5 in lista:
    cinco = 'faz parte da lista'
else:
    cinco = 'não faz parte de lista'
print('-='*30)
print(f'Você digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ondem decrescente são {lista}')
print(f'O valor 5 {cinco}')

"""
valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    continuar = ' '
    while continuar not in 'SsNn':
        continuar = str(input('Quer continuar? [S/N]: ')).strip() 
    if continuar in 'Nn':
        break
print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')
print('O valor 5 faz parte da lista' if 5 in valores else 'O valor 5 não foi encontrado na lista!' )
    
"""
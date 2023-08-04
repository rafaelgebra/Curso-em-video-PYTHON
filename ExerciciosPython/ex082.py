lista_geral = []
lista_pares = []
lista_impares = []
while True:
    n = (int(input('Digite um numero: ')))
    lista_geral.append(n)
    if n % 2 == 0:
        lista_pares.append(n)
    elif n % 2 == 1:
        lista_impares.append(n)
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print('-'*30)
print(f'A lista completa é {lista_geral}')
print(f'A lista de pares é {lista_pares}')
print(f'A lista de impares é {lista_impares}')


"""
total_Lista = []
par_Lista = []
impar_Lista = []
while True:
    num = int(input('Digite um número: '))
    total_Lista.append(num)
    continuar = ' '
    while continuar not in 'SsNn':
        continuar = str(input('Quer continuar? [S/N]: ')).strip()
    if num % 2 == 0:
        par_Lista.append(num)
    elif num % 2 == 1:
        impar_Lista.append(num)
    if continuar in 'Nn':
        break
print('-='*30)
print(f'A lista completa é {total_Lista}')
print(f'A lista de pares é {par_Lista}')
print(f'A lista de impares é {impar_Lista}')


EX: 2

lista_Total = []
lista_pares = []
lista_Impares = []
while True:
    num = int(input('Digite um numero: '))
    lista_Total.append(num)
    
    continuar = ' '
    while continuar not in 'NnSs':
        continuar = str(input('Quer continuar? ')).strip()
    if continuar in 'Nn':
        break
for pos, numeros in enumerate(lista_Total):
    if numeros % 2 == 0:
        lista_pares.append(numeros)
    else:
        lista_Impares.append(numeros)
print(f'A lista completa é {lista_Total}')
print(f'A lista de pares é {lista_pares}')
print(f'A lista de ímpares é {lista_Impares}')




"""
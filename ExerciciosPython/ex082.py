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
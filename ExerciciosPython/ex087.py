matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_Par = soma_Coluna3 = maior_Valor = 0
for linha in range(0, 3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
print('-='*30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz [linha][coluna] % 2 == 0:
            soma_Par += matriz[linha][coluna]
    print()
print('-='*30)
print(f'A soma dos valores pares é {soma_Par}')
for linha in range(0, 3):
    soma_Coluna3 += matriz[linha][2]
print(f'A soma dos valores da terceira coluna é {soma_Coluna3}')
for coluna in range(0, 3):
    if coluna == 0:
        maior_Valor =  matriz[1][coluna]
    elif matriz[1][coluna] > maior_Valor:
        maior_Valor = matriz[1][coluna] 
print(f'O maior valor da segunda linha é {maior_Valor}')


"""

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_Par = 0
soma_Coluna3 = 0
maior_Valor = 0
cont = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor [{linha}, {coluna}]: '))
print('='*20)
print(f'{"Matriz em PYTHON":-^20}')
print('='*20)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
print('='*20)
for numero in matriz:
    soma_Coluna3 += numero[2]
    for valor in numero:
        if valor % 2 == 0:
            soma_Par += valor
print(f'A soma dos valores pares é {soma_Par}')
print(f'A soma dos valores da terceira coluna é {soma_Coluna3}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')


Ex: 2

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_Par = soma_Terceira_C = maior_Valor_segunda_L = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valore para [{l, c}]: '))
        soma_Terceira_C += matriz[l][2]
        if matriz[l][c] % 2 == 0:
            soma_Par += matriz[l][c]
        if c == 0 :
            maior_Valor_segunda_L = matriz[1][c]
        else:
            if matriz[1][c] > maior_Valor_segunda_L:
                maior_Valor_segunda_L = matriz[1][c]
print('-'*60)
for l in range(0, 3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print()
print('-'*60)
print(f'A soma dos valore pares é {soma_Par}')
print(f'A soma dos valores da terceira coluna é {soma_Terceira_C}')
print(f'O maior valor da segunda linha é {maior_Valor_segunda_L}')

"""
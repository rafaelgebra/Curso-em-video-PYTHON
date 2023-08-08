matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
print('-='*30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()

"""
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for x in range(0,3):
    for y in range(0, 3):
        matriz[x][y] = (int(input(f'Digite um valor para [{x, y}]: ')))
   
print(matriz)
for x in range(0, 3):
    for y in range(0, 3):
        print(f'[{matriz[x][y]:^5}]', end=' ')
    print()

    
Ex: 2


matriz2 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz2[l][c] = int(input(f'Digite um valore para [{l, c}]: '))
print(matriz2)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz2[l][c]:^7}]', end=' ')
    print()

"""
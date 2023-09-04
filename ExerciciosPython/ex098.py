from time import sleep
def contador(i, f, p):
    print(f'Contagem de {inicio}, até {fim}, de {passo} em {passo}')
    for c in range(inicio, fim, passo):
        print(f'{c}', end=' ')
    print()


"""print('-=' * 50)
for c in range(0, 11, 1):
    print(f'{c}', end=' ')
print()
print('-=' * 50)
for c in range(10, -1, -1 ):
    print(f'{c}', end=' ')
print()"""




inicio  = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))


contador(1, 11, 1)
contador(10, 0, -1)
contador(inicio, fim, passo)
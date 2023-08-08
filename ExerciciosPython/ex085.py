principal = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        principal[0].append(valor)
    else:
        principal[1].append(valor)
print('-='*30)
principal[0].sort()
principal[1].sort()
print(f'Os valores pares digitados foram: {principal[0]}')
print(f'Os valores ímpares digitados foram: {principal[1]}')


"""
principal = []
par = []
impar = []
for c in range(1, 8):
    principal.append(int(input(f'Digite o {c}º valor: ')))
for valor in principal:
    if valor % 2 == 0:
        par.append(valor)
        principal.clear
    elif valor % 2 == 1:
        impar.append(valor)
        principal.clear
print('-='*30)
par.sort()
print(f'Os valores pares digitados foram: {par}')
impar.sort()
print(f'Os valores ímpares digitados forom: {impar}')



Ex: 2



lista = [[], []]
for c in range(1, 8):
    num = int(input(f'Digite o {c}º valore: '))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
lista[0].sort()
lista[1].sort()
print(f'Os valores pares digitados foram {lista[0]}')
print(f'Os valores ímpares digitados foram {lista[1]}')

"""
temporario = list()
principal = list()
total_Pessoas = mais_Leve = mais_Pesada = 0
while True:
    total_Pessoas +=1 
    temporario.append(str(input(f'Digite o nome da {total_Pessoas}º pessoa ? ')))
    temporario.append(int(input(f'Qual o peso da {total_Pessoas}º pessoa ? ')))
    if len(principal) == 0:
        mais_Leve = mais_Pesada = temporario[1]
    else:
        if temporario[1] < mais_Leve:
            mais_Leve = temporario[1]
        if temporario[1] > mais_Pesada:
            mais_Pesada = temporario[1]       
    principal.append(temporario[:])
    temporario.clear() 
    continuar = ' '
    while continuar not in 'NnSs':
        continuar = str(input('Quer continuar? [S/N]: '))
    if continuar in 'Nn':
        break
print('-'*60)
print(f'Ao todo foram cadastrados {total_Pessoas} pessoas. ') # Também pode ser feito com len(principal)
print(f'O maior peso doi de {mais_Pesada}Kg. Peso de,', end=' ')
for p in principal:
    if p[1] == mais_Pesada:
        print(f'{p[0]} ', end='')
print()
print(f'O menor peso foi de {mais_Leve}Kg. Peso de, ', end=' ')
for p in principal:
    if p[1] == mais_Leve: 
        print(f'{p[0]} ',end='')
print()


"""

dados = list()
princ = list()
total_Pessoas = 0
mais_Leve = mais_Pesada = 0
cont = 0
while True:
    total_Pessoas +=1 
    dados.append(str(input(f'Digite o nome da {total_Pessoas}º pessoa ? ')))
    dados.append(int(input(f'Qual o peso da {total_Pessoas}º pessoa ? ')))
    if len(princ) == 0:
        mais_Leve = mais_Pesada = dados[1]
    else:
        if dados[1] < mais_Leve:
            mais_Leve = dados[1]
        elif dados[1] > mais_Pesada:
            mais_Pesada = dados[1]
        cont += 1
    princ.append(dados[:])
    dados.clear()
    continuar = ' '
    while continuar not in 'NnSs':
        continuar = str(input('Quer continuar? [S/N]: '))
    if continuar in 'Nn':
        break
print(f'Foram cadastradas {total_Pessoas} pessoas')
print(f'O maior peso foi de {mais_Pesada}Kg. Peso de ', end=', ')
for pessoa in princ:
    if pessoa[1] == mais_Pesada:
        print(f'{pessoa[0]} ', end='')
print()
print(f'O menor peso foi de {mais_Leve}Kg. ', end=', ')
for pessoa in princ:
    if pessoa[1] == mais_Leve:
        print(f'{pessoa[0]} ', end='')
print()


"""
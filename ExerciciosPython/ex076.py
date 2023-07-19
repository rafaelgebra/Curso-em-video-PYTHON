listagem = ('Lápis', 1.75, 'Borracha', 2.00 )
print(f'{"LISTAGEM DE PREÇOS":^50}')
for elemento_Listagem in range(0, len(listagem)):
    if elemento_Listagem % 2 == 0:
        print(f'{listagem[elemento_Listagem]:.<40}R$', end=' ')
    else:
        print(f'{listagem[elemento_Listagem]:>5.2f}')

continuar = ' '
homens = 0
mm20 = 0
total = 0
while continuar != 'N':
# pode ser colocado while True:
# para ser eterno. porem tem que colocar o break no fim.
        idade = int(input('Idade: '))
        sexo = ' '
        while sexo not in 'MF':
            sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
        continuar = ' '
        while continuar not in 'SN':
            continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if sexo == 'F' and idade <= 20:
            mm20 += 1
        if sexo == 'M':
            homens += 1
        if idade >= 18:
            total += 1
        #if constinuar == 'N'
        #   break
print(f'Total de pessoas com mais de 18 anos sao {total}')
print(f'Ao total temos homem {homens} cadastrados' )
print(f'Temos {mm20} mulheres com menos de 20 anos')


"""

total18 = homens = mulheres = 0
while True:
    print('='*30)
    print(f'{"CADASTRE UMA PESSOA":^30}')
    print('='*30)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('[M/F]: ')).strip().upper()[0]
    continuar = ' '
    if idade >= 18:
        total18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade <= 20:
        mulheres += 1
    while continuar not in 'SN':    
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {total18}.')
print(f'Ao todo temos {homens} homens cadastrados.')
print(f'Ao todo temos {mulheres} mulheres cadastradas com menos de 20 anos')


"""
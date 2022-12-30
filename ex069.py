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
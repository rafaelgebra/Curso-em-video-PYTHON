pessoa = {}
total_Pessoas = []
total_Idade = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: ')).strip()
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F]')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Escolha M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    total_Idade += pessoa['idade']
    total_Pessoas.append(pessoa.copy())
    while True:
        continuar = str(input('Quer continuar? ')).strip().upper()[0]
        if continuar in 'SN':
            break
        print('ERRO! Digite S ou N. ')
    if continuar == 'N':
        break
print(f' A) Ao total temos {len(total_Pessoas)} pessoas cadastradas')  
media =  total_Idade / len(total_Pessoas)
print(f' B) a média de idade é {media:5.2f} anos')
print(f' C) As mulheres cadastradas foram: ',end='')
for pessoa in total_Pessoas:
   if pessoa['sexo'] in 'F':
        print(f'{pessoa["nome"]}', end=', ')
print()
print(f' D) A lista das pessoas que estão acima da média é:')
for pessoa in total_Pessoas:
    if pessoa['idade'] >= media:
        print('   ', end='')
        for keys, value in pessoa.items():
            print(f'{keys} = {value}; ', end='')
        print()
print('  << ENCERRANDO>>  ')


"""




"""
ficha = []
while True:
    nome = str(input('Nome: ')).strip()
    nota1 = float(input('Nota1: '))
    nota2 = float(input('Nota2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    continuar = ' '
    while continuar not in 'NnSs':
        continuar = str(input('Quer continuar? [S/N] '))
    if continuar in 'Nn':
        break
print('='*60)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print('='*60)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*60)
    opcao = int(input(f'Mostrar notas de qual aluno? (999 interrompe): '))
    if opcao == 999:
        print('FINALIZANDO...')
        break
    if opcao <= len(ficha) -1:
        print(f'Notas de {ficha[opcao][0]} são {ficha[opcao][1]}')
    else:
        print('Opção invalida! Tente outra vez')
print('FIM')
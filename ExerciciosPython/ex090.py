dados = {}
dados['nome'] = str(input('Nome? ')).strip()
dados['media'] = float(input(f'Média de {dados["nome"]}: '))
print('-'*50)
if dados['media'] >= 7:
    dados['situacao'] = 'APROVADO'
    print('APROVADO')
elif 5 <= dados['media'] < 7:
    dados['situacao'] = 'RECUPERAÇÃO'
else:
    dados['situacao'] = 'REPROVADO'
    print('REPROVADO')
print('-'*50)    
for keys, values in dados.items():
    print(f'  - {keys} é igual a {values}')

"""
aluno = {}
aluno['nome'] = str(input('Qual o nome do aluno? '))
aluno['media'] = float(input(f'Qual a média de {aluno["nome"]}? '))

if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'Recuperação'
elif aluno['media'] < 5:
    aluno['situação'] = 'Reprovado'
else:
    print('ERRO... Tente novamente!!')
print('-'*50)
for keys, values in aluno.items():
    print(f'{keys} é igual a {values}')


"""
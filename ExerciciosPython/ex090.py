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


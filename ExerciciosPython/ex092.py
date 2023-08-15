from datetime import date # ou from datetime import datetime
ano = date.today().year 
dados = {}
dados['nome'] = str(input('Nome: '))
nascimento = int(input('Nome de Nascimento: '))
dados['idade'] = ano - nascimento # pode fazer assim no luagar de ano -> idade = datetime.now().year
dados['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if dados['ctps'] > 1:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salario'] = int(input('Salario: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - ano)
print('-'*40)
for keys, values in dados.items():
    print(f'  --{keys} tem o valor {values}')

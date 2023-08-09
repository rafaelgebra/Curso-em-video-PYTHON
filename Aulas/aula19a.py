dados = {'nome':'Pedro', 'idade':25} # ou dados = dict('nome':'Pedro', 'idade':25)
print(dados['nome'])
print(dados['idade'])
dados['sexo'] = 'M' # adicionar elementos
print(dados)
del dados['idade'] # remover elemento
print(dados)

filme = {   # O python chama esses elementos "titulos, ano, diretor" de chaves ou 'keys'
    'titulo':'Star Wors',
    'ano':1977,
    'diretor':'George Lucas',
}
# o que é itens, chaves e valor?

#print(filme.values()) -> Values é um metodo interno # vai retornar todos os valores
print('Nesse exemplo vai retornar os:') # 'Star Wors', 1977, 'George Lucas'
print(filme.values())

#print(filme.keys()) -> Vai retornar as chaves que nesse caso é.
print('Nesse exemplo vai retornar os:') # 'titulo', 'ano', 'diretor'
print(filme.keys())

#print(filme.items()) -> Vai retornar tanto os valores quanto as chaves.
print('Nesse exemplo vai retornar os:')
print(filme.items()) # [('titulo', 'Star Wors'), ('ano', 1977), ('diretor', 'George Lucas')]

for k, v in filme.items(): # para cada chave, e valor em filme.items():
    print(f'O {k} é {v}') # o K é a chave e o V é o valor

locadora = [{'titulo':'Star Wors', 'ano':1977, 'diretor':'George Lucas'}, {'titulo':'Avengres', 'ano':2012, 'diretor':'Joss Whedon'}, {'titulo': 'Matrix', 'ano':1999, 'diretor':'Wachowski'}]

print(locadora[0]['ano'])
print(locadora[2]['titulo'])

pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas)
print(pessoas['nome'])
print(pessoas['idade'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')# tem que ter aspas duplas "", por estar dentro de aspas simples''.
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
print('-'*40)

cont = 0    
for keys, values in pessoas.items():
    print(f'A pessoas {pessoas["nome"]} tem {pessoas["idade"]} anos de idade')
    cont += 0
    if cont <= 1:
        break

print('-'*40)
for values in pessoas.values():
    print(values)
print('-'*40)

for keys in pessoas.keys(): # para cada uma das 'chaves' em pessoas.keys()
    print(keys)
print('-'*40)

del pessoas['sexo']
for k, v in pessoas.items():
    print(f'{k} = {v}')
print('-'*40)

pessoas['peso'] = 68.5 # Para o dicionario não é nescessario usar o .append pode ser feito direto.
pessoas['nome'] = 'rafael'
for k, v in pessoas.items():
    print(f'{k} = {v}')
print('-'*40)

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'Rio de Jeneiro', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(estado1)
print(estado2)
print(brasil)
print(brasil[0])
print(brasil[1])
print(brasil[0]['uf'])
print(brasil[1]['sigla'])


estado = {}
brasil = []
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
print(brasil)
print('-'*50)
for estado in brasil:
    print(estado)
print('-'*50)
for estado in brasil:
    for keys, values in estado.items():
        print(f'O campo {keys} tem valor {values}')
for estado in brasil:
    for values in estado.values():
        print(f'{values}', end=' ')
    print()
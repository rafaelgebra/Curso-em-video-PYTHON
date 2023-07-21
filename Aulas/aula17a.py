# aula 17 LISTAS
'''Diferente das tuplas as listas podem sem manipuladas(multaveis)'''

                () TUPLA - CHAVES
                [] LISTA - COLCHETES
                {} dicionario

'''para adicionar "itens" no FINAL uma lista tem que usar o comando .append()'''
.append(item)
'''Tambem pode adicionar item no meio ou qualquer lugar da lista usando o comando .insert(0, 'iten')'''
.insert(0, 'item') # neste caso mostra que esta acidionando o item na posição 0 da lista

'''Eliminar item da lista pode ser feita polos comandos'''
del item [3] #comando basico # usando essa formula se deleta pelo indice.
item.pop(3) #normalmente é usando esse comando para eliminar o ultimo elemento da lista, mas se passar os paremetros desejamos ele apaga o item # usando essa formula se deleta pelo indice.
item.pop() #dessa forma só elimina o ultimo elento.
item.remove('item') # usando essa formula se deleta conteudo/item

'''para remover algum item da lista mas não sabe se esse item tem na lista
só usar a formula '''
if item in lista:
    lista.remove('item')

#criar lista atravez de range
valores = list(range(4,11)) # sera comocado tudo isso dentro de uma lista chamado valores que é o nome da vareavel e será identificado como uma lista normal
'''range cria uma lista organizada mas se quiser fazer uma lista fora de ontem tem que fazer manual.'''
'''Mas se a lista estiver fora de ondem e quiser deixar em ondem usar o metodo. lista. sort() '''
lista.sort() #ordena todos os valores deixanso em ondem
'''se quiser deixar ondem inverza. '''
lista.sort(reverse=True)
'''tamanho da lista, só usar a função len função interna'''
len(lista)

"""from random import randint # Fim com que os numeros fozem escolidos aleatoriamente pela funcao randint
valores = list()
print(randint)
cont = randint(0, 10)
for l in range(0, 5):
    cont += randint(0, 100000)
    valores.append(cont)
for c, v in enumerate(valores):
    print(f'Na posicao {c} encontrei a valore {v}! ')
print('Cheguei ao final da lista')"""
valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um numero ')))
for c, v in enumerate(valores):
    print(f'Na posicao {c} encontrei o valor {v}!')
print('Cheguei ao final da lista ')


a = [2, 3, 4, 7]
b = a # isso nao é uma copia é uma ligação entre elas
b = a[:] # para fazer uma copia da LISTA tem que usar o fatiameno senao o que mudar em uma muda na outra
print(f'Lista {a}')
print(f'Lista {b}')
b [2] = 8
print(f'Lista {a}')
print(f'Lista {b}')


lanche = ['Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata frita']
print(lanche)
print(lanche[3])
lanche[3] = 'Picole'
print(lanche)
lanche.append('Cooke')# o metodo .append() adiciono o 'itém' no final da lista.
print(lanche)
lanche.insert(0,'Cachorro-quente')
print(lanche)

"""    Apagando itém de uma lista             """

del lanche[3] # foi deletado a Pizza que é o indice 3 "posição 4". # É usado nesse caso os Colchetes []
print(lanche)
lanche.pop(3) # agora será deletado o que esta no indece 3 que antes era a Pizza. # Nessa caso é usado os Parênteses ()
print(lanche)
lanche.pop() # Normalmente é usado para excluir o ultimo elemento, mas se passar os parametros dentro do Paêeteses () pode excluir um itém especifico
print(lanche)
lanche.remove('Hambúrguer') # Já nessa opção, NÃO se coloca o valor do índece entre os Parênteses mas sim o 'VALOR'/'ITÉM' 
print(lanche)
if 'Hamburguer' in lanche:
    print(lanche.remove('Hamburguer'))
else:
    print('O item Hamburguer não tem mais nessa lista')


"""                 Criando listas atravez de RANGE            """
valores=list(range(4,11,2))
print(valores)

valores2 = [8,2,5,4,9,3,0]
print(valores2)
valores2.sort() # Esse metodo deixar organizado/ordenar crescente
print(valores2)
valores2.sort(reverse=True) # Esse metodo deixar organizado/ordenar decrescente
print(valores2)
print(len(lanche)) # metodo função interna do python, mostra o tamanha 
print(len(valores)) # metodo função interna do python, mostra o tamanha
print(len(valores2)) # metodo função interna do python, mostra o tamanha
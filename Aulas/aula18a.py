"""             Aula 18 - LISTAS - Parte 2              """
# Lista dentro de lista.

dados1 = ['Pedro', 25]
dados2 = ['Maria', 19]
dados3 = ['João', 32]

pessoas = [dados1,dados2,dados3]
print(dados1) # imprime o conteúdo da lista dados1
print(dados2) # imprime o conteúdo da lista dados2
print(dados3) # imprime o conteúdo da lista dados3
print(pessoas) # imprime o conteúdo da lista pessoas
print(pessoas[0])
print(pessoas[0][0])   
print(pessoas[1][1])
print(pessoas[2][0])


"""         Exemplo 1           """

test = []
test.append('Gustavo')
test.append(40)

galera = list()
galera.append(test[:])
print(galera)
test[0] = 'Maria'
test[1] = 22
galera.append(test[:])

print(galera)

"""         Exemplo 2           """

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
#print(galera[0][0])
for pessoa in galera:
    print(f'{pessoa[0]:<8} tem ', end='')
    print(f'{pessoa[1]} anos de idade.')


"""         Exemplo 3           """

galera = list()
dados = list()
total_Maior = total_Menor = 0
for c in range(0,3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:]) # não pode esquecer os simbulas [:], senão os dados não são copiados
    dados.clear()
for pessoa in galera:
    if pessoa[1] >= 21:
        print(f'{pessoa[0]} é maior de idade.')
        total_Maior += 1
    else:
        print(f'{pessoa[0]} é menor de idade. ')
        total_Menor += 1
print(f'Temos {total_Maior} maiores e {total_Menor} menores ')

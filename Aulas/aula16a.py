# Tuplas () é uma varíavel composta e IMUTÁVEL.
# No Python as tupla não é mais obrigatório os parenteses ()

'''
Para acessar os elementos de uma tupla ultiliza o indice que inicia em 0.

'''

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata frita')
#lanche1 = ['Hambúrguer', 'Suco', 'Pizza', 'Pudim'] - LISTA
#lanche2 = {'Hambúrguer', 'Suco', 'Pizza', 'Pudim'} - DICIONARIO
print(lanche)
print(lanche[2])
print(lanche[0:2])
print(lanche[1:])
print(lanche[-1])
print(len(lanche))
print(f'{"FIM":=^50}')

for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra carambra')
print(f'{"FIM":=^50}')


for pos, c in enumerate(lanche):
    if c in 'Suco':
        print(f'Eu vou beber {c}')
    print(f'Eu vou comer {c} na posição {pos}')
print('Comi pra caramba')
print(f'{"FIM":=^50}')
#print(lanche1)
#print(lanche2)
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição', end=' ')
    print((cont))
print('Comi pra caramba')
print(f'{"FIM":=^50}')


""" Com a função print(sorted(lanche)) ORGANIZADO/ORDEM"""
print(sorted(lanche[:3]))
print(sorted(lanche))
print(lanche)

print(f'{"Fim do exemplo LANCHE":=^100}')


a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(a+b)
print(c)
print(len(c))
print(c.count(5))
print(c.index(5, 2)) # para seber a posição de um número usar a função interna .index, caso tenha o mesmo número em mais de uma posição, informar mais uma vez dentro da função .index """ EX print(c.index(5, 2) o "cinco" indica qual o número a ser procurado no index, o "2 " indica qual a posição do index que é para começar o outro número. """
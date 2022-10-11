import random
alu1 = str(input ('Qual o nome do primeiro aluno? '))
alu2 = str(input('Qual o nome do segundo aluno ? '))
alu3 = str(input('Qual o nome do segundo aluno? '))
alu4 = str(input('Qual o nome do quarto aluno? '))
lista = [alu1, alu2, alu3, alu4]
random.shuffle(lista)
print('O nome do aluno sortiado e')
print(lista)
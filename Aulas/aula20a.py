 Aula 20 - FUNÇÕES


# Para declarar uma função personalizada usar a "palavra - def"

#           Ex: 1
def mostralinha():
    print('-'*30)

mostralinha()
print(f'{"SISTEMA DE ALUNOS":^30}')
mostralinha()
mostralinha()
print(f'{"CADASTRO DE FUNCIONÁRIOS":^30}')
mostralinha()
mostralinha()
print(f'{"ERRO DO SISTEMA":^30}')
mostralinha()

#           Ex: 2

def mensagem(msg): # O msg é um parametro
    print('-'*30) #Aqui é uma linha
    print(msg) # aqui é uma mensagem que vai 'vir' como paremetro.
    print('-'*30) #Aquei é uma linha


mensagem(f'{"SISTEMA DE ALUNOS":^30}')
mensagem(f'{"APRENDDNDO PYTHON":^30}')
mensagem(f'{"RAFAEL RODRIGUES GEBRA":^30}')


#           Ex: 3
def titulo(txt):
    print('-'*30)
    print(txt)
    print('-'*30)


titulo(f'{"SISTEMA DE ALUNOS":^30}')
titulo(f'{"APRENDDNDO PYTHON":^30}')
titulo(f'{"RAFAEL RODRIGUES GEBRA":^30}')
titulo(f'{"TO CHEGANDO":^30}')


"""a = 4
b = 5
s = a + b
print(s)
s = 8
b = 9
s = a + b
print(s)
a = 2
b = 1
s = a + b
print(s)"""

def soma(a, b):
    s = a + b
    print('-'*30)
    print(s)


soma(4, 5)

# além disso posso mudar a ordem

def soma2(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')

soma2(b=4, a=5)
soma2(7, 9)



pares = []
impares = []

def par (num):
    print('-')
    if num % 2 == 0:
        print(f"O número {num} é par")
        pares.append(num)

    else:
        print(f'O número {num} é impar')
        impares.append(num)

for c in range(0, 8):
    par(int(input('Digite um número ')))

   
print(pares)
print(impares)


# Isso NÃO é DESEMPACOTAMENTO é lista.
def dobra(lst):
    pos = 0
    while pos < len(valores):
        lst[pos] *= 2
        pos += 1

valores = [6, 5, 2, 8, 0]
dobra(valores)
print(valores)



# Isso é DESEMPACORAMENTO
def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando o valores {num} é igual a {s}')


soma(5, 2)
soma(2, 9, 4)
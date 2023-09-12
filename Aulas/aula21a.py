                    # Curso em Python - Aula 21 - Funções (Parte 2)

# 1º Interactive help - Ajuda interativa

# A primeira forma é usar a função/metodo - help() NO CONSOLE.
"""
Para ter essa 'Ajuda' no Pycharm é só ir Console Python e escrever a função/metodo - help()

Para ter essa 'Ajuda' no VScode é so abre o console e escrever Python depois escreve a função/metodo - help() 'no caso do VScode tem que apertar a letra Q para poder ter outra ajuda'.


"""
# A segunda forma é usar a função/metodo - help() dentro do "programa".
"""
Tanto dentro do Pycharm e do VScode é do escrever dentro do programa a função/metodo - help(print)
Esse é um exemplo. mas pode por qualquer função dentro de help()
"""

# A terceira forma é usar o doc interno dentro de um comando - __doc__
"""
Tando dentro do Pycharm e do VScode é usado da seguinte forma.
Ex: parametros do comando input. 
print(input.__doc__) "as informações talvez não sejam tão parecidas"
"""


# 2º Docstrings - String de documentação - As nossos funções podem ser documentadas

def contador(i, f, p): # i, f, p São chamados de parametros Reais 
    #para criar um docstring dessa função é só abrir aspas duplas 3 vezes aqui em baixo
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Função criada por rafael cursando Python no Curso em Vídeo
    """
    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c += p
    print('FIM!')

#Programa Principal
contador(1, 10, 2) # 1, 10, 2 = São chamados de paramentros Formais
help(contador)


# 3º Argumentos/Parametros opcionais

def somar(a=0, b=0, c=0): # esse =0 é chamado de parametro opcional
    """
    -> Faz a soma de três valores e mostra o resultado na tela.
    :param a: o primeiro valor
    :param b: o segundi valor
    :param c: o terceiro valor
    """
    s = a + b + c
    print(f'A soma vale {s}')

#Programa Principal
somar(3, 2, 5)
somar(3, 2)
somar(3)
somar()
# para não tem problema com quantidade de parametros tem que usar a técnica de multi parametros - def somar(*num):

help(somar) #docstring


# 4º Escopo de variáveis - normalmente escopo é o local aonde uma variável vai existir e aonde a variável não vai mais existir.

# Ex:1
def test():
    x = 8 # Variável/Escopo local - esse Escopo só funciona dentro da função/local
    print(f'Na função teste n vale {n}')
    print(f'Na função teste x vale {x}')

#Programa Principal
n = 2 # Variável/Escopo global
print(f'No programa principal, n vale {n}')
test()

#Ex:2
def teste(b):
    a = 8   # Escopo local
    b += 4  # Escopo local 
    c = 2   # Escopo local
    print(f'(A) dentro vale {a}')
    print(f'(B) dentro vale {b}')
    print(f'(C) dentro vale {c}')


#Programa Principal
a = 5 # Escopo global
print(f'(A) fora vale {a}')
teste(a)

#Ex: 3
def teste(b):
    global a
    a = 8   # Escopo local
    b += 4  # Escopo local 
    c = 2   # Escopo local
    print(f'(A) dentro vale {a}')
    print(f'(B) dentro vale {b}')
    print(f'(C) dentro vale {c}')


#Programa Principal
a = 5 # Escopo global
print(f'(A) fora vale {a}')
teste(a)
print()
print(f'(A) fora vale {a}')
teste(a)

# 5º Retorno de resultados

#Ex: 
def somar(a=0, b=0, c=0):
    s = a + b + c
    return s
    
r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)
print(f'Meus cálculos deram {r1}, {r2}, {r3}')


# Pratica

#Ex: 1 - Fatorial

def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f
    
n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')


#Ex: 2

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False
for c in range(0, 4):  
    print()  
    num = int(input('Digite um numero: '))
    if par(num):
        print('É par')
    else:
        print('É impar')




Dica -> Para não pular linha usar (end=' ') depois de:
print('A soma e {}  e a divisao e {:.3f} '.format(s, d), end=' ') no final da linha.

DICA -> print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')


                () TUPLA
                [] LISTA
                {} dicionario

# , (end='') nao quebra a linha
# (\n) quebra linha


'Aula 6 - tipos primitivos e saída de dados'  


Para escrever uma string dentro de um print serve tanto aspas simples como duplas, porém a comunidade recomenda por aspas simples -  então siga a recomendação.

Os quatro tipos primitivos mais basicos que existem são:

int -> 'número inteiro = 7, -4, 0, 9875 '

float   -> 'números reais, flotuantes = 4.5, 0.0076, -15.223'

bool -> 'Booleanos, valor lógico = True ou False (Sempre coma primeira letra MAIÚSCULA)'

str -> 'caracter, string =' 'Olá', '7,5', ''


PARA VER O TIPO é só usar:
print(type())

Dica -> No caso abaixo, a Variável "num" é um OBJETO e todo objeto tem caracteristicas e realiza funcionalidades, com isso tem ATRIBUTOS e METODOS.

#Tudo que vem depois do (num.is...)é um metodo


num = input('Digite algo ')
print('Foi digitado o seguinte {}, qual o tipo {} '.format(num, type(a)))
print('so tem espaco {} '.format(num.isspace()))
print('E um numero? {}'.format(num.isnumeric()))
print(f'É alfanumerico? {num.isalnum()}')
print('É alfabetico? {}'.format(num.isalpha()))
print('Esta em maiusculas? {}'.format(num.isupper()))
print('Esta em minusculas? {}'.format(num.islower()))
print(f'Esta capitalozada? {num.istitle()}')


'Aula 7 - operadores Aritméticos'

+   -> adição
-   -> subtração
*   -> Multiplicação
/   -> Divisão
**  -> Potência
//  -> Divisão inteira
%   -> Resto da divisão (modulo)


#ORDEM de PRECEDÊNCIA dentro de Operadores Aritméticos

1   ()              -> Parenteses
2   **              -> Potência   
3   *, /, //, %     -> Multiplicação, Divisão, Divisão Inteira, Resto da Divisão 
4   +, -            -> Soma, Subtração

{'='*20} Vai aparecer = 20 vezes
{:>20}  Vai aparecer o conteudo alinhado a DIREITA com 20 espaços 
{:<20}  Vai aparecer o conteudo alinhado a ESQUERDA com 20 espaços 
{:^20}  Vai aparecer o conteudo CENTRALIZADO com 20 espaços 
{:=^20} Vai aparecer o conteudo alinhado com = em volta do conteúdo com 20 espaços 

                'Aula 8 - Utilizando Módulos'

Importar dados/modulos.
tem duas maneiras basicas de importar modulos no Python

1- comando import (importa dodas as funcionalidades do módulo)

2- from......import.... (importar somente um contéudo da bíblioteca )

Ex: usando o modulo completo 

import math
num = int(input('Digite um numero:'))
raiz = math.sqrt(num)
arr = math.ceil(raiz)
bai = math.floor(raiz)
print('A raiz de {} é {:.2f} e arredondada para cima é {} e arredondado para baixo é {}'.format(num, raiz, arr, bai))


#Para arredondar para cima usar assim. porém o valor é inteiro
print('A raiz de {} é {}' .format(num, math.ceil(raiz)))

#Para arredondar para baixo. poŕem o valor é inteiro
print('A raiz de {} é {} arredondando para baixo é' .format(num, math.floor(raiz)))

Ex:
Usando só algumas funcionalidades do módulo

from math import sqrt, ceil, floor
num = int(input('Digite um numero:'))
raiz = sqrt(num)
arr = ceil(raiz)
bai = floor(raiz)
print('A raiz de {} é {:.2f} e arredondada para cima é {} e arredondado para baixo é {}'.format(num, raiz, arr, bai))

#Para arredondar para cima usar assim. porém o valor é inteiro
print('A raiz de {} é {}' .format(num, ceil(raiz)))

#Para arredondar para baixo. poŕem o valor é inteiro
print('A raiz de {} é {} arredondando para baixo é' .format(num, floor(raiz)))

                'Aula 9 - Fratiamento de string'

frase = 'Curso em Video Python'
print(frase[9]) -> 'Significa que o python vai pegar o caracter 9'
print(frase[:15] -> )
print(frase[9:15] -> 'Significa que é pra pegar do caracter 9 até o 14, não pega a o ultimo porque o python o ultimo é excluido ')
print(frase[9:21] -> 'Nessa frase o caracter 21 nao existe. ate da para usar porque esta um caracter acimada maxima, mas nao a melhor forma de utilizar.')
print(frase[9:21:2] -> 'começa no 9 caracter e vai até o 21 caracter porem saltando de 2 em 2')
print(frase[:5] -> 'quando nao tem o caracter inicial vai ate o caracter 5')
print(frase[15:] -> 'Significa que sabe ainde comeca a contar os caracter mas nao tem a indicacao do fim da string entao vai ate o sim dela, "nesse casa tem a palavra 'PYTHON'"')
print(frase[9::3]) -> 'Comeca no 9 e vai ate o fim, porem tem o :3 que siguinifica pular de 3 em 3'

'''analise'''
'Analisa uma string e muito importante, tamanho, qual letra comeca ou termina...'
print(len(frase)) #len significa comprimento#
print(frase.count('o')) #count significa contar#
print(frase.count('o',0,13)) #o puthon ja faz uma contagem com fatiamento#
print(frase.find('deo')) #find significa encontrar # -> find mostra aonde comecou a procura
print(frase.find('Android')) -> 'Quando a streng nao existe ou nao encontrado o python retorna -1'
print('Curso' in frase) ->  'in significa, em ou tem' '{se tem a palavra o python retorna TRUE}' "in nao e uma funcao e um operador mas da para fazer analize"

''' Transformacao'''
"""Uma lista de string e imutavel, ms consegue mexer com os metodos"""
print(frase.replace('Python','Android')) # replace significa trocar/reposicionar
print(frase.upper()) # tudo maiuscolo e obrigatorio os () no final
print(frase.lower())   # tudo minisculo e obrigatorio os () no final
print(frase.capitalize()) # so a primeira letra maiuscolo, e obrigatorio no final ()
print(frase.title()) # a primeira letra da palavra fica maiusculo(consegue fazer isso pela posicao dos espacos, e obrigatorio no final ()
print(frase.strip()) # remove todos os espacos inuteis no fim e no comeco
print(frase.rstrip()) # remove somente os ultimos espacos (lado da direita)
print(frase.lstrip()) # remove somente os primeros especas (lado esquerdo)

'''Divisao'''
print(frase.split()) # por padrao uma divicao entro da str considerando os espacos
        'Curso em Video Python'
        '01234 01 01234 012345'

'''Juncao'''
print('-'.join(frase))
        'Curso em Video Python'
        '01234 01 01234 012345'
'com join (juntar) consegue juntar uma coisa na outro, no caso de ("Curso em Video Python" vira uma str unica "Curso-em-Video-Python" porque foi selecionado - no lugar de espaco)'


frase2 = '   Aprenda Python  '
print(frase2)
print(frase2.strip()) # remove os espacos da direita e esquerda
print(frase2.rstrip()) # remove os espacos da direita
print(frase2.lstrip()) # remoce os espacos da esquerda



frase = 'Curso em Vídeo Python'
print(frase.upper().count('O'))
print(len(frase.strip()))
print(frase.replace('Python', 'Android'))
print(frase)
print('Curso' in frase)
print(frase.find('Curso'))
print(frase.lower().find('vídeo'))

dividido = frase.split() # transforma em uma lista
print(dividido) #['Curso', 'em', 'Vídeo', 'Python' / transforma cada palavra em um índice separado
print(dividido[0]) # Curso / foi celecionado o itém 0 da lista
print(dividido[2][3]) # e / foi celecionado o a letra referente ao índece 3 do itém 2 da lista



# importar data #
from datetime import date
ano = date.today().year


#print('Tipo primitivos')

#('int-inteiro')ex('7,-4,0,9875')
#('float-reais')ex('4.5,0.075,-15.223,7.0')
#('bool-boleano')ex('true,folse')
#('str-string')ex('ola,','','7.5')

#Formato antigo da sintaxi do print ('A soma entre ',pri,'e',seg,'e igual a', soma)
#Formato atualizado da sintaxi do print('A soma entre {}'.format())

# Operadores aritimeticos
# + Adicao
# - Subtracao
# * Mulplicacao
# / Divicao
# ** Potencia
# // Divisao Inteira
# % Resto da Divisao (modolo)

# Dentro de uma expressao aritimerica
#       Ordem de precedencia
#       1 ()
#       2 **
#       3 *,/,//,%
#       4 +,-

# quantas casas decimais mostrar na .format{:.2f}

# Raiz quadrada, n1**(1/2) ou (pow(n1,(1/2)

# , (end='') nao quebra a linha
# (\n) quebra linha

# Biblioteca math (matematica)
    # ceil = teto (para cima)
    # fllor = para baixo
    # trunc = eleminar da virgular
    # pow = potencia
    # sqrt = raiz quadrada
    # factorial = fatorial

# Para usar a biblioteca inteira usar o comando
# EX: import math
# importar comando especifico usar o comando direto
# EX: from math import fllor

# == IGUAL
# != DIFERENTE

# comando de contagem tempo#
from time import sleep
'''jogador = int(input('Qual e a sua jogada '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)'''



        '''Aula 13'''

# estruturas de repetição #
# Laço,repetições, iteração #

# primeira estrutura de repetição #

''' a estrutura de repeticao + o contador = faco com variavel de controle'''

''' o comando de faço '''
n = int(input('digite um numero.'))
for c in range(0, 5):
    if n <= 9:
        print(c)

""" randomizando Auternando os numeros"""
from random import randint
cumputador = randint(0, 5).

print(cumputador)

# Emojis #
Para usar o emoji fazer a seguinte seguência

U+1F386 # ESSE é o codigo so emoji

print('U0001F386') # no codigo alterar o sinal de + e 3 zeros. pronto


'Teste logico par com' if# if numero % 2 == 0:#


#Estrutura condicional no Python

# se = if
# senao = else
# e = and
# or = ou
# elif = senao se = else if

#se carro.esquerda() = ifcarro.esquerda():
#    bloco_V_            bloco True
#senao               = else:                Nao esquecer os : pontos
#    bloco_F_            bloco False

"""tempo = int(input('Quantos anos tem seu carro'))
if tempo <=3:
    print('carro novo')
else:
    print('carro velho')
# simplificado
#print('carro novo'if tempo <= 3 else 'carro velho')
print('--FIN--')"""

"""nome = str(input('Qual o seu nome? '))
if nome == 'Rafael':
    print('Que nome lindo voce tem!')
else:
    print('Que nome normal voce tem {}'.format(nome))
print('Bom dia, {}'. format(nome))"""


# estruturas de repetição #
# Laço,repetições, iteração #

# primeira estrutura de repetição #

''' a estrutura de repeticao + o contador = faco com variavel de controle'''

''' comando de faço 
i = int(input('Inicio. '))
f = int(input('Fim: '))
p = int(input('Passo'))
for c in range(i, f+1, p):
    print(c)
print('FIM')'''

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor '))
    s += n #'''Isso e a mesma coisa que (s = s + n)'''#
print('O somatorio de todos os valores sao {}'.format(s))

# AULA 14 #

# ESTRUTURA DE REPETICAO CONTESTE LOGICO (WHILE) #
''' while not "apple":
    "passo"
"pega"
'''                # Estrutura#
'''    enquanto nao "apple"            while not "apple":
        se "chao"                       if "chao"
            "anda"                          "anda"
        se "buraco"                     if "buraco"
            "pula"                          "pula"
        se "moeda"                      if "moeda"
            "pega"                          "pega"
    "pega"                          "pega"
'''

'''from time import sleep
for c in range(1, 10):
    print(c, end=' ')
    sleep(0.2)
print('FIM')'''
from time import sleep
c = 1
while c < 10:
    print(c)
    sleep(0.2)

    c += 1
print(https://animesonline.cc/episodio/urusei-yatsura-2022-episodio-2/'FIM')

"""como mostrar o valor do maior e menor numero"""

if cont == 1:
    maior = menor = num
    else:
    if num > maior:
        maior = num
    if num < menor:
        menor = num

# Aula 15 - Interrompendo repeticoes while
'''Laco de repeticao parte 3 '''

'''função interrompa'''
#quando utilizar break (interrompa) é utilidado quando precisa parar/quedar um loop"""


'''considerar um numero par ou impar/divizivelpor 0'''

print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')

if tipo == 'P':
    if total % 2 == 0:
        print('Voce VENCEU!')
    v += 1
    else:
    print('Voce PERDEU')
    break
elif tipo == 'I':
    if total % 2 == 1:
    print('Voce VENCEU!')
    v += 1
    else:
    print('Voce PERDEU')
    break
print()

""" nao aceita enquanto nao por as insformacoes corretas"""
while sexo not in 'MF':
    sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]


# Aulas 16 - Tuplas
"""Nessa aula, vamos aprender o que são TUPLAS e como utilizar tuplas em Python. 
As tuplas são variáveis compostas e imutáveis que permitem armazenar vários valores em uma mesma estrutura, 
acessíveis por chaves individuais."""

# As tuplas SÃO IMUTÁVEIS

                () TUPLA
                [] LISTA
                {} dicionario


#Para criar uma tupla, tem que usar parenteses ()
#O Python apartir do 3.6 não precisa mais por os ()
#       Manipular/Fatiar uma tupla.
lanche = ('Hambúrguer', 'Suco', ' Pizza', 'Pudin')
print(lanche[0]) #'''Mostra somente o primeiro posição que começa sempre em 0 na tupla'''
print(lanche[1:3]) # mostra o elenento Suco pois ele esta na segunda posição, quer esta na primeira posição e o Hambúrguer que é a posição 0.
print(lanche[:3]) #'''Mostra a primeira posição pois nao tem indicação de quando começar, mais termina na três e mostra somente a posição dois,
#isso acontece porque no Python não considera a leitura da ultima posição'''
print(lanche[-4]) #'''Faz uma contagem regreciva da ultima para a primeira'''
print(lanche[-3:]) #'''Indica que vai começar uma contagem regreciva e vai contar menos tres elemento e vai até o fim da tupla'''
print(len(lanche[0]))

for comida in lanche:
    print(f'Eu vou comer {comida}')

print('-'*20)
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi pra caramba')
print('-'*20)
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('-'*20)

# soma de tuplas NÃO DE VALORES
a = (2, 3, 4)
b = (5, 8, 1 ,2)
c = a + b #A ondem dos faltores alteram o resultado
print(c)
"""em tuplas não se soma os valores das tuplas mas se somam o conteudo as tuplas"""
print('-'*20)

pessoa = ('Rafael', 34, 'M', 78)
print(pessoa)
del(pessoa)
pessoa = (1,2,3,4,5)
print(pessoa)

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




"""             EXEMPLO DE EXERCICIO               """

num = [2, 5, 9, 1, 2,]
print(num)
num[2] = 3
num.append(7)
print(num)
#num.sort(reverse=True)
print(num)
#num.sort()
print(num)
num.insert(2, 0)# Insere um item no local escolhido, nessa caso o 2 é a posição do índice e o 0 é o itém a ser acrescentado sem remover o atual
print(num)
num.pop() # remove o ultimo item da lista
print(num)
num.pop(2) # remove o itém que está no índice selecionado que esta pelos Parênteses
print(num)

for número in num:
    if 3 in num:
        num.remove(3) # remove o "conteúdo"/"valor" que esta dentro dos Parênteses # caso tenha mais iténs com as mesma caracteristicas, tem que usar os laços para remover, póis o .remove() só remove o primeiro itém da lista.
for número in num:
    if 2 in num:
        num.remove(2)
print(num)

print(f'Essa lista tem {len(num)} elementos')


"""                 EXEMPLO             """

valores = []
for c in range(0,5):
    valores.append(int(input('Digite os valores: ')))
for pos, valor in enumerate(valores):
    print(f'Na posição {pos} encontrei o valor {valor}... ')
print('Cheguei nessa MEEEEERDAA')


"""             Explicação de ligação e cópia de lista          """

a = [2, 3, 4, 7]
b = a # Quando se cria uma igualdade na lista, o python entende que tem um ligação entre elas então se mexe em uma a outra também é alterada. Para fazer uma copia tem que fazer o seguinte b = a[:] -> isso signifaca que b esta recenbendo todos os iténs de a
c = a[:]
c[2] = 1

print(f'Lista A: {a}')
print(f'Lista B: {b}') # Aqui os "dados" da lista é uma ligação com a lista A. 
print(f'Lista C: {c}') # Aqui os "dados" da lista é uma copia da lista A.




#               Aula 19 - Dicionários


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


#               Aula 20 - FUNÇÕES em programação podemos dizer que é uma rotina
#
# # Para declarar uma função personalizada usar a "palavra - def" definição de função
#
# #           Ex: 1
# def mostralinha():
#     print('-'*30)
#
# mostralinha()
# print(f'{"SISTEMA DE ALUNOS":^30}')
# mostralinha()
# mostralinha()
# print(f'{"CADASTRO DE FUNCIONÁRIOS":^30}')
# mostralinha()
# mostralinha()
# print(f'{"ERRO DO SISTEMA":^30}')
# mostralinha()
#
# #           Ex: 2
#
# def mensagem(msg): # O msg é um parametro
#     print('-'*30) #Aqui é uma linha
#     print(msg) # aqui é uma mensagem que vai 'vir' como paremetro.
#     print('-'*30) #Aquei é uma linha
#
#
# mensagem(f'{"SISTEMA DE ALUNOS":^30}')
# mensagem(f'{"APRENDDNDO PYTHON":^30}')
# mensagem(f'{"RAFAEL RODRIGUES GEBRA":^30}')
#
#
# #           Ex: 3
# def titulo(txt):
#     print('-'*30)
#     print(txt)
#     print('-'*30)
#
#
# titulo(f'{"SISTEMA DE ALUNOS":^30}')
# titulo(f'{"APRENDDNDO PYTHON":^30}')
# titulo(f'{"RAFAEL RODRIGUES GEBRA":^30}')
# titulo(f'{"TO CHEGANDO":^30}')
#
#
# """a = 4
# b = 5
# s = a + b
# print(s)
# s = 8
# b = 9
# s = a + b
# print(s)
# a = 2
# b = 1
# s = a + b
# print(s)"""
#
# def soma(a, b):
#     s = a + b
#     print('-'*30)
#     print(s)
#
#
# soma(4, 5)
#
# # além disso posso mudar a ordem
#
# def soma2(a, b):
#     print(f'A = {a} e B = {b}')
#     s = a + b
#     print(f'A soma de A + B = {s}')
#
# soma2(b=4, a=5)
# soma2(7, 9)
#
#
#
# pares = []
# impares = []
#
# def par (num):
#     print('-')
#     if num % 2 == 0:
#         print(f"O número {num} é par")
#         pares.append(num)
#
#     else:
#         print(f'O número {num} é impar')
#         impares.append(num)
#
# for c in range(0, 8):
#     par(int(input('Digite um número ')))
#
#
# print(pares)
# print(impares)
#
#
# # Isso NÃO é DESEMPACOTAMENTO é lista.
# def dobra(lst):
#     pos = 0
#     while pos < len(valores):
#         lst[pos] *= 2
#         pos += 1
#
# valores = [6, 5, 2, 8, 0]
# dobra(valores)
# print(valores)
#
#
#
# # Isso é DESEMPACORAMENTO
# def soma(*valores):
#     s = 0
#     for num in valores:
#         s += num
#     print(f'Somando o valores {num} é igual a {s}')
#
#
# soma(5, 2)
# soma(2, 9, 4)
#
# # exemplos praticos
#
# def l(msg):
#     tam = len(msg)+4
#     print('-'*tam)
#     print(f'  {msg}  ')
#     print('-' *tam)
#
#
# def soma(a, b):
#     s = a + b
#     l(f'A soma entre {a} + {b} é {s}')
#
#
# def valores(*num):
#     s = 0
#     for valor in num:
#         print(f'{valor}', end=' ')
#         s += valor
#     print(f'O soma dos valores sao {s}')
#
#
# def dobra(*num):
#     for valor in num:
#         print(f'O valor dobrado de {valor} é ', end='')
#         valor *= 2
#         print(valor)
#     print()
#
#
# def dobranum(lis):
#     pos = 0
#     while pos < len(lis):
#         lis[pos] *= 2
#         pos += 1
#
#
#
# #Programa Principal
# l('Curso em Video')
# l('Aprendendo Python')
# l('Rafael Rodrigues')
# soma(2, 4)
# soma(b=4, a=7)
# soma(1, 2)
# valores(5, 7, 3, 1, 4)
# valores(8, 4, 7)
# valores(2, 4)
# valores()
# dobra(7, 2, 5, 0, 4)
# lista = [7, 2, 5, 0, 4]
# dobranum(lista)
# print(lista)


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

def contador(i, f, p):  # i, f, p São chamados de parametros Reais
    # para criar um docstring dessa função é só abrir aspas duplas 3 vezes aqui em baixo
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


# Programa Principal
contador(1, 10, 2)  # 1, 10, 2 = São chamados de paramentros Formais
help(contador)


# 3º Argumentos/Parametros opcionais

def somar(a=0, b=0, c=0):  # esse =0 é chamado de parametro opcional
    """
    -> Faz a soma de três valores e mostra o resultado na tela.
    :param a: o primeiro valor
    :param b: o segundi valor
    :param c: o terceiro valor
    """
    s = a + b + c
    print(f'A soma vale {s}')


# Programa Principal
somar(3, 2, 5)
somar(3, 2)
somar(3)
somar()
# para não tem problema com quantidade de parametros tem que usar a técnica de multi parametros - def somar(*num):

help(somar)  # docstring


# 4º Escopo de variáveis - normalmente escopo é o local aonde uma variável vai existir e aonde a variável não vai mais existir.

# Ex:1
def test():
    x = 8  # Variável/Escopo local - esse Escopo só funciona dentro da função/local
    print(f'Na função teste n vale {n}')
    print(f'Na função teste x vale {x}')


# Programa Principal
n = 2  # Variável/Escopo global
print(f'No programa principal, n vale {n}')
test()


# Ex:2
def teste(b):
    a = 8  # Escopo local
    b += 4  # Escopo local
    c = 2  # Escopo local
    print(f'(A) dentro vale {a}')
    print(f'(B) dentro vale {b}')
    print(f'(C) dentro vale {c}')


# Programa Principal
a = 5  # Escopo global
print(f'(A) fora vale {a}')
teste(a)


# Ex: 3
def teste(b):
    global a
    a = 8  # Escopo local
    b += 4  # Escopo local
    c = 2  # Escopo local
    print(f'(A) dentro vale {a}')
    print(f'(B) dentro vale {b}')
    print(f'(C) dentro vale {c}')


# Programa Principal
a = 5  # Escopo global
print(f'(A) fora vale {a}')
teste(a)
print()
print(f'(A) fora vale {a}')
teste(a)


# 5º Retorno de resultados

# Ex:
def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)
print(f'Meus cálculos deram {r1}, {r2}, {r3}')


# Pratica

# Ex: 1 - Fatorial

def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')


# Ex: 2

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

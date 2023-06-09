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


num = input('Digite algo ')
print('Foi digitado o seguinte {}, qual o tipo {} '.format(num, type(a)))
print('so tem espaco {} '.format(num.isspace()))
print('E um numero? {}'.format(num.isnumeric()))
print(f'É alfanumerico? {num.isalnum()}')
print('É alfabetico? {}'.format(num.isalpha()))
print('Esta em maiusculas? {}'.format(num.isupper()))
print('Esta em minusculas? {}'.format(num.islower()))
print(f'Esta capitalozada? {num.istitle()}')



'Aula 9'

'''Fratiamento de string'''

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
print(frase2.strip()) # remove os espacos da direota e esquerda
print(frase2.rstrip()) # remove os espacos da direita
print(frase2.lstrip()) # remoce os espacos da esquerda

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

# Aulas 15 - Tuplas
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
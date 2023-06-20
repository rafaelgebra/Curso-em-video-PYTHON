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

    Ex:

nome = str(input('Qual o seu nome? ')).strip().upper()
if nome == 'RAFAEL':
    print('Que nome lindo, {}!' .format(nome))
else:
    print('Seu nome é tão normal {}'. format(nome))
print('Bom dia!!')

    Ex:

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
m = (n1 + n2)/2
"""if m >= 7:
    print('Parabéns você foi aprovado')
else:
    print('Você é muito burro, NÃO foi aprovado')"""
print('Parabéns você foi aprovado' if m >= 7 else 'Você é muito burro, Não foi aprovado') # simplificado
print('A sua média é {:.2f}'.format(m))


EXERCICIO 28 

import random
from time import sleep # Essa função faz con que demore algum tempo para continuar a leitura da linha de comando
com = random.randint(0, 5) # "PENSAR" na realidade esta sorteando o número aleatório.
print('-=-'*30)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*30)

num = int(input('Em que número eu pensei? '))
print('Processando...')
sleep(2) # o conteudo dentro do () é os segundos de espera
if num >= 0 and num <= 5:
    if num == com:
        print('Parabéns você acertou!!')
    else:
        print('Você errou, tente novamente!!')
elif num >= 6:
        print('Número invalido!!')
        print('Tente novamente!!')



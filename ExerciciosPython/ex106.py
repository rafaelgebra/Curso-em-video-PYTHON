# Faça um mini-sistema que ultiliza o interactive Help do python. O usuário vai digitar o comando e p manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: Use cores.
from time import sleep
c = ('\33[m',           # 0 - sem cores
     '\33[0;30;41m',    # 1 - Vermelho
     '\33[0;30;42m',    # 2 - verde
     '\33[0;30;43m',    # 3 - amarelo
     '\33[0;30;44m',    # 4 - azul
     '\33[0;30;45m',    # 5 - roxo
     '\33[7;30m'        # 6 - branco
     )


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com} \'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def titulo(msg, cor=0):
    tam = len(msg) +4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}  ')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


#Programa Principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA', 2)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO', 1)

'''
from time import sleep
c = ['\33[m',
     '\033[0;30;41m',
     '\033[0;30;42m',
     '\033[0;30;43m',
     '\033[0;30;44m',
     '\033[0;30;45m',
     '\033[7;30m']


def ajuda(msg, cor=0):

    titulo(f'acessando o manual do comando \'{msg}\'', 3)
    sleep(1)
    print(c[5], end='', flush=True)
    return help(msg)


def titulo(msg, cor=0):

    tam = len(msg) + 4
    sleep(1)
    print(c[cor], end='')
    print('~' * tam)
    print(msg)
    print('~' * tam)
    print(c[0], end='')


while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    sleep(1)
    palavra = str(input('Função ou Bibliotera > '))
    if palavra.upper() == 'FIM':
        break
    else:
        ajuda(palavra)
titulo('ATÉ LOGO', 1)


'''
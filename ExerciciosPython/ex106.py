# Faça um mini-sistema que ultiliza o interactive Help do python. O usuário vai digitar o comando e p manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: Use cores.

c = ('\33[m',           # 0 - sem cores
     '\33[0;30;41m',    # 1 - Vermelho
     '\33[0;30;42m',    # 2 - verde
     '\33[0;30;43m',    # 3 - amarelo
     '\33[0;30;44m',    # 4 - azul
     '\33[0;30;45m',    # 5 - roxo
     '\33[7;30m',       # 6 - branco
     )

def ajuda(com):
    help(com)

def titulo(msg, cor=0):
    tam = len(msg) +4
    print(c[cor],end='') 
    print('~' * tam)
    print(f'  {msg}  ')
    print('~' * tam)
    print(c[0],end='')

#Programa Principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA', 1)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO', 2)
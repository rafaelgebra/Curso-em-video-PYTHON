from time import sleep

def area(larg, comp):
    total = largura * comprimento
    print(f'A área de um terreno de {largura:.1f}x{comprimento:.1f} é {total:.1f}m²')
    sleep(1)

def p():
    print('-'*40)

def iteracao(txt):
    print(txt)
    sleep(1)



while True:
    p()
    print(f'{"Controle de Terrenos":^40}')
    p()
    largura = float(input('LARGURA (m): '))
    comprimento = float(input('COMPRIMENTO (m): '))
    iteracao('Carregando...')
    iteracao('O resultado é')
    area(largura, comprimento)
    while True:
        continuar = str(input('Quer continuar? [S/N]')).strip()[0]
        if continuar in 'SsNn':
            break
        print('Opção inválida. Digite S ou N. ')
    if continuar in 'Nn':
        break

#Exemplo sw exercio 2

"""
from time import sleep
def mensagem(txt):
    """
    -> Faz a leitura da mensagem e deixa formatada
    :param txt: recebe a mensagem e escreve com linha em baixo
    :return: sem retorno
    """
    tam = len(txt) + 4
    print('-' * tam)
    print(f'  {txt}  ')
    print('-'*tam)


def area(l, c):
    """
    -> Faz a leitura do terreno
    :param l: parametro de largura
    :param c: paramentro de comprimento
    :return: sem retorno
    """
    area = l * c
    print(f'A área de um terreno {l}x{c} é de {area}')


#Programa Principal
mensagem('Controle de Terreno')
while True:
    largura = float(input('LARGURA (m): '))
    sleep(0.4)
    comprimento = float(input('COMPRIMENTO (m): '))
    sleep(0.4)
    area(largura, comprimento)
    sleep(1)
    while True:
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if continuar in 'SN':
            break
        print('Opção invalida! Digite S ou N.')
    if continuar == 'N':
        break
sleep(1)
print('FIM')

"""
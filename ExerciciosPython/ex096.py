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


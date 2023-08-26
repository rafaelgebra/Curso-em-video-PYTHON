from time import sleep
def aria():
    total = largura * comprimento
    print(f'A área de um terreno de {largura:.1f}x{comprimento:.1f} é {total:.1f}m²')
    sleep(1)
def p():
    print('-'*40)
def iteracao(txt):
    
    print(txt)
    sleep(1)
for c in range(0, 2):
    p()
    print(f'{"Controle de Terrenos":^40}')
    p()
    largura = int(input('LARGURA (m): '))
    comprimento = int(input('COMPRIMENTO (m): '))
    
    if c == 4:
        iteracao('FIM')
        iteracao('O resultado é')
        aria()
    else:
        iteracao('Carregando...')
        iteracao('O resultado é')
        aria()


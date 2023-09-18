def escreva(txt):
    tam = len(txt) + 4
    print('~' * tam) # pode ser feito assim também
    print(f'  {txt}  ')
    print('~' * (len(txt) + 4)) # pode ser feito assim também


# Programa principal
escreva('Rafael')
escreva('Estudando Python')
escreva('Curso em Vídeo')


"""
def escreva(txt):
    tam = len(txt)+4
    print('~'*tam)
    print(f'  {txt}  ')
    print('~'*tam)


#Programa Principal
while True:
    escreva('Gustavo Guanabara')
    escreva('Curso em Vídeo no YouTube')
    escreva('CeV')
    while True:
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if continuar in 'NS':
            break
        print('Opção invalida!! Digite somente S ou N.')
    if continuar == 'N':
        break
escreva('FIM... Obrigado por participar')


"""
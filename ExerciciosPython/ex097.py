def escreva(txt):
    tam = len(txt) + 4
    print('~' * tam) # pode ser feito assim também
    print(f'  {txt}  ')
    print('~' * (len(txt) + 4)) # pode ser feito assim também


# Programa principal
escreva('Rafael')
escreva('Estudando Python')
escreva('Curso em Vídeo')
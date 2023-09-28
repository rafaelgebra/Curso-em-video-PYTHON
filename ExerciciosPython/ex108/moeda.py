def metade(v=0):

    return v / 2


def dobro(v=0):

    return v * 2


def aumentar(a=0, b=0):
    valor = a + (a * b) / 100

    return valor


def diminuir(a=0, b=0):
    valor = a - (a * b) / 100

    return valor


def moeda(v=0, moeda='R$'):
    return f'{moeda}{v:>.2f}'.replace('.',',')

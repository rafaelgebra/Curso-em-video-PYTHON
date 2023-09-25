
def fatorial(num=0, show=False):
    """
    -> Calcula o Fatorial de um número
    :param n: o número a ser calculado
    :param show: mostra ou não a conta
    :return: O valor fatorial de um número n.
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ' , end='')
            else:
                print(' = ', end='')
        f *= c
    print(f)
    return f # retorno não estafuncionando 12/09/2023


#Programa Princial
n = int(input('Digite um número: '))
print(f'O fatorial do numero de {n} é...', end=' ')
fatorial(n, show=True)



'''
from time import sleep
def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número
    :param n: O número a ser calculado
    :param show: (opcional) mostra ou não o calcúlo
    :return: O valor do Fatorial de um número n
    """
    f = 1
    print('-'*40)
    for c in range(n, 0, -1):
        if show:
            print(c, end='', flush=True)
            sleep(1)
            if c > 1:
                print(f' x ', end='', flush=True)
            else:
                print(f' = ', end='', flush=True)
        f *= c
    return f


num = int(input('Digite um número: '))
print(fatorial(num, show=True))
help(fatorial)

'''
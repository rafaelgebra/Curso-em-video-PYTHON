def fatorial(num=0, show=False):
    """
    -> Calcula o Fatorial de um número
    :param n: o número a ser calculado
    :param show: mostra ou não a conta
    :return: O valor fatorial de um número n.
    """
    f = 1
    for c in  range(num, 0, -1):
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
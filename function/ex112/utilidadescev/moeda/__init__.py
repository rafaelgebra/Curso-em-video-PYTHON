def metade(preço=0, formato=False):
    valor: float = (preço / 2)

    return valor if formato is False else moeda(valor)


def dobro(preço=0, formato=False):
    valor = preço * 2
    return valor if formato is False else moeda(valor)


def aumentar(preço=0, taxa=0, formato=False):
    valor = preço + (preço * taxa) / 100
    return valor if formato is False else moeda(valor)


def diminuir(preço=0, taxa=0, formato=False):
    valor = preço - (preço * taxa) / 100
    return valor if formato is False else moeda(valor)


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:>.2f}'.replace('.',',')


def resumo(preço=0, taxaa=10, taxar=5):
    print('-' * 30)
    print(f'{"RESUMO DO VALOR".center(30)}')
    print('-' * 30)
    print()
    print(f'{"Preço analisado:":<20} \t{moeda(preço)}')
    print(f'{"Dobo do preço:":<20} \t{dobro(preço, True)}')
    print(f'{"Metade do preço:":<20} \t{metade(preço, True)}')
    print(f'{f"{taxaa}% de aumento:":<20} \t{aumentar(preço, taxaa, True)}')
    print(f'{f"{taxar}% de redução:":<20} \t{diminuir(preço, taxar, True)}')
    print('-'*30)



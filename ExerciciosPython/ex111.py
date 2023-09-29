from ex111.utilidadescev import moeda


p = float(input(('Digite o preço: R$')))
taxaa = int(input('Qual a TAXA de aumento? '))
taxar = int(input('Qual a TAXA de redução? '))
moeda.resumo(p, taxaa, taxar)

from utilidadescev import moeda
from utilidadescev import dado

p = dado.leia_Dinheiro('Digite o preço: R$')
taxaa = int(input('Qual a TAXA de aumento? '))
taxar = int(input('Qual a TAXA de redução? '))
moeda.resumo(p, taxaa, taxar)


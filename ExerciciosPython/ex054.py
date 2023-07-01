from datetime import date
ano = date.today().year
cont = 0
cont1 = 0
for c in range(1, 8):
    nasc = int(input('Em que ano a {} pessoa nasceu? '.format(c)))
    idade = ano - nasc
    print(idade)
    if idade > 21:
        cont += 1
    elif idade < 21:
        cont1 += 1
print('Ate o momento existem {} pessoas que ainda nao atigiram a maior idade'.format(cont1))
print('Ate o momento existem {} pessias que ja atingiram a maoir idade'.format(cont))
from datetime import date
ano_Atual = date.today().year
maior = 0
menor = 0

for c in range(1, 8):
    nasc = int(input('Em que ano a {}º pessao nasceu? ' .format(c)))
    idade = ano_Atual - nasc
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('Até o ano de {} tem {} maior de idade e {} menor de idade'.format(ano_Atual, maior, menor))




"""

"""
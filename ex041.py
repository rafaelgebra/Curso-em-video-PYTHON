from datetime import date
# "nasc" significa data de nascimento
nasc = int(input('Qual o ano de nascimento do atleta? '))
# tanto "ano" como "ano2" e a data atual da maquina.
ano = date.today().year
ano2 = date.today().year
# "it" significa idade atual
it = ano-nasc
# a formula e baseada na questao matematica da idade como "ano-nasc" da um numero inteiro entao fiz a base da idade e categoria
if ano-nasc <=9:
    ano = 'Mirim'
    it = ano2-nasc
elif (ano-nasc >9) and (ano-nasc <=14):
    ano = 'Infantil'
    it = ano2-nasc
elif (ano-nasc > 14) and (ano-nasc <= 19):
    ano = 'Junior'
    it = ano2-nasc
elif (ano-nasc >19) and (ano-nasc <= 20):
    ano = 'Senior'
    it = ano2-nasc
else:
    print('O atleta tem mais de 20 ano entao esta na categoria MASTER')
print('O atleta esta na categoria {} pois tem {}'.format(ano,it))
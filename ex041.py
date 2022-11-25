from datetime import date
# "nasc" significa data de nascimento
nasc = int(input('Qual o ano de nascimento do atleta? '))
# "ano" e a data atual da maquina.
ano = date.today().year
# "it" significa idade atual
it = ano-nasc
# a formula e baseada na questao matematica da idade como "ano-nasc" da um numero inteiro entao fiz a base da idade e categoria
if ano-nasc <=9:
    it = ano - nasc
    ano = 'Mirim'
elif (ano-nasc >9) and (ano-nasc <=14):
    it = ano - nasc
    ano = 'Infantil'
elif (ano-nasc > 14) and (ano-nasc <= 19):
    it = ano - nasc
    ano = 'Junior'
elif (ano-nasc >19) and (ano-nasc <= 20):
    it = ano - nasc
    ano = 'Senior'
elif (ano-nasc > 20):
    it = ano - nasc
    ano = 'MASTER'
print('O atleta esta na categoria {} pois tem {} anos. '.format(ano, it))
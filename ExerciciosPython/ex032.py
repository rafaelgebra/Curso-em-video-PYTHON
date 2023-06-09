from datetime import date
ano = int(input('Que ano quer analizar? Coloque  0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano que voce digitou {}{}{} e BISSEXTO'.format('\033[33m', ano, '\033[m'))
else:
    print('O ano que voce digitou {}{}{} NAO e BISSEXTO'.format('\033[34m', ano, '\033[m'))

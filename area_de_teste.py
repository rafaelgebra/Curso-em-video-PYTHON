from datetime import date
ano = int(input('Que ano você nasceu: '))
ano_atual = date.today().year
idade = ano_atual - ano

print(idade)

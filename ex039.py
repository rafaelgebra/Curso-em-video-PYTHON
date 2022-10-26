from datetime import date
nas = int(input('Qual o seu ano de nascimento? '))
ano = date.today().year
if nas > (ano-18):
    print('Voce ainda nao tem idade para de alistar no exercito brasileiro, falta {} anos'.format(ano-nas))
elif nas < (ano-18):
    print('Ja deveria estar alistado, vode esta atrazado a {} anos'.format(ano-nas-18))
elif nas == ano or ano:
    print('deu ruim')

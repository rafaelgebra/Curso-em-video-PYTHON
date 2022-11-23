from datetime import date
nas = int(input('Qual o seu ano de nascimento? '))
ano = date.today().year
sex = str(input('Qual o seu Sexo? ')).lower()
if sex == 'm':
    if nas > (ano-18):
        print('Voce ainda nao tem idade para de alistar no exercito brasileiro, falta {} anos'.format(ano-nas))
    elif nas < (ano-18):
        print('Ja deveria estar alistado, voce esta atrazado a {} anos'.format(ano-nas-18))
    elif nas == ano or ano:
        print('deu ruim')
elif sex == 'f':
    print('Voce nao precisa de alistar!')
else:
    print('opcao invalida. Entente novamente.')
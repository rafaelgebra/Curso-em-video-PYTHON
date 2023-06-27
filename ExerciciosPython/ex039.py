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



"""
from datetime import date
ano = int(input('Que ano você nasceu: '))
sexo = str(input('Qual o seu Sexo? ')).strip().upper()
ano_atual = date.today().year
idade = ano_atual - ano

print('Quem nasceu em {} tem {} anos em {}.' .format(ano, idade, ano_atual))
if sexo == 'M':
    if idade < 18: 
        saldo = 18 -idade
        print('Falta {} anos para se alistar.' .format(saldo))
        print('Seu alistamento será {} '.format(ano + 18)) 
    elif idade == 18:
        print('Deve se alistar  imediatamete!!')
    else:
        saldo = idade - 18
        print('Já passou do tempo faz {}' .format(saldo))
        print('Seu alistamento foi em {}' .format(ano +  18))
else:
    print('Para o sexo Feminino não é obrigatorio')
"""
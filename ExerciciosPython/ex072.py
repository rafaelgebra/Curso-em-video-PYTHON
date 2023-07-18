cont = ('zero', 'um', 'dois', 'três', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze',
        'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
continuar = 'S' # essa linha foi colocada para o while dar inicio ao loop.
while continuar != 'N':
    if continuar == 'N':
        break
    numeros = int(input('Digete um numero entre 0 e 20: '))
    if numeros >= 0 and numeros <= 20:
        print(f'você digitou o numero {cont[numeros]}') # O elemento da tupla e acessado pelos parenteses [].
        continuar = str(input('Quer continar? [S/N] ')).upper().strip()[0]
    else:
        numeros = int(input('Tente novamente. Digete um numero entre 0 e 20: '))
print('Obrido por participar!!')


"""
tupla = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','dose','treze','quatorze','quize','dezeseis','dezesete','dezoito','dezenove','vinte')

continuar = 'S'
while continuar != 'N':
    if continuar == 'N':
        break
    num = int(input('Digite um número entre 0 e 20: '))
    if num >= 0 and num <= 20:
        print(f'Você digitou o numero {(tupla[num])}')
        continuar = str(input('Quer continuar? ')).strip().upper()
    else:
        num = int(input('Tente vamente. Digite um número entre 0 e 20: '))"""


"""num = int(input('Digite um número entre 0 e 20: '))
continuar = 'S'
while True:
    if continuar in 'Nn':
            break
    if 0 <= num <= 20:
        print(f'Você digitou o número {tupla[num]}')
        continuar = str(input('Quer continuar? [S/N] ')).strip()
    else:
        num = int(input('Tente novamente. Digite um número entre 0 e 20: '))
"""

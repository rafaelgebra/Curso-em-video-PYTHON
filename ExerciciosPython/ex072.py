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

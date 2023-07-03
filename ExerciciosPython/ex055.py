maior = 0
menor = 0
for pessoa in range(1, 6):
    peso = float(input('Peso da {}o pessoa: '.format(pessoa)))
    if pessoa == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('A maior peso lido foi de {}Kg,'.format(maior))
print('O menor peso lido foi de {}Kg,'.format(menor))
print('A media entre o maior e menor peso e de {}Kg'.format(maior/menor))


"""
maior = 0
menor = 0   
for c in range(1,6):
    peso = float(input('Peso da {}º pessoa: ' .format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {:.2f} Kg' .format(maior))
print('o menor peso lido foi de {:.2f} Kg' .format(menor))

"""
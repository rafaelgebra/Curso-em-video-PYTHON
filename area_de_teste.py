maior = 0
menor = 0   
for c in range(1,6):
    peso = int(input('Peso da {}º pessoa: ' .format(c)))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print('O maior peso lido foi de {:.2f}' .format(maior))
print('o menor peso lido foi de {:.2f}' .format(menor))




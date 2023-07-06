n = 1
totpar = 0
totinpar = 0
cont = 1
while n != 0:
    n = int(input('Digite um {}º valor: ' .format(cont)))
    cont += 1
    if n != 0:
        if n % 2 == 0:
            totpar += 1
        if n % 2 == 1:
            totinpar += 1

print('O total de números pares é {}' .format(totpar))
print('O total de números impares é {}' .format(totinpar))
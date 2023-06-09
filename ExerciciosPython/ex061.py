primeiro = int(input('Primeiro termo "NUMERO": '))
razao = int(input('Razao "PULAR": '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{}'.format(termo), end='-> ')
    termo += razao
    cont += 1
print('FIM')
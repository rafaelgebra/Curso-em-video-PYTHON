primeiro = int(input('Primeiro termo "NUMERO" '))
razao = int(input('Razao "PULAR" '))
decimo = primeiro + (10-1) * razao
for c in range(primeiro, decimo + razao, razao):
    print('{}'.format(c), end='-> ')
print('FIM')
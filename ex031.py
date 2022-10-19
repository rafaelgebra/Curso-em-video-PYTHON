km = int(input('Qual a distancia da viagem em KM? '))
v1 = 0.50
v2 = 0.45
if km <= 200:
    print('o valor da viagem sera {}{}{}'.format('\033[35m', km*v1, '\033[m'))
else:
    print(('O valor da viagem sera {}{}{}'.format('\033[36m', km*v2, '\033[m')))
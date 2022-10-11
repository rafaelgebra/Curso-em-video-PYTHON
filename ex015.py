km = float(input('Quanto Km foram rodados com o carro? '))
dias = int(input('Foi alugado por quantos dias? '))
valorkm = 0.15 * km
valordias = 60 * dias
pagar = valorkm + valordias
print('O valor a ser pago por {} dias de aluguel e {} \ne foram gatos R${} de combustivel \no valor total a pagar e {}'.format(dias, valordias, valorkm, pagar))
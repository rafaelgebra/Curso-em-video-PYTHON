num = int(input('Um numoro de 4 digitos '))
n = str(num)
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o numero {}'.format(num))
print('Unidade {}'.format(n[3]))
print('Dezena {}'.format(n[2]))
print('Centena {}'.format(n[1]))
print('milhar {}'.format(n[0]))
print('Analisando o numero (2) {}'.format(num))
print('Unidade {}'.format(u))
print('Dezena {}'.format(d))
print('Centena {}'.format(c))
print('Minhar {}'.format(m))

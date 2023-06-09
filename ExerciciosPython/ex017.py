from math import hypot
co = float(input('Digite a valor do cateto oposto '))
ca = float(input('Digite o valor do cateto adjacente '))
hipo = hypot(co,ca)
hi = (co ** 2 + ca ** 2) ** (1/2)
print('O valor da Hipotenusa e {:.2f}'.format(hipo))
print('O valor da Hipotenusa e {:.2f}'.format(hi))
''' '''
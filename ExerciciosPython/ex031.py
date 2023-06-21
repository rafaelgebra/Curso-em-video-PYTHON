km = int(input('Qual a distancia da viagem em KM? '))
v1 = 0.50
v2 = 0.45
if km <= 200:
    print('o valor da viagem sera {}{}{}'.format('\033[35m', km*v1, '\033[m'))
else:
    print(('O valor da viagem sera {}{}{}'.format('\033[36m', km*v2, '\033[m')))


"""from time import sleep
distancia = int(input('Qual a distancia da sua viagem? '))
abaixo200 = 0.5 * distancia
acima200 = 0.45 * distancia
print('Você está preste a começar uma viagem de {}Km '.format(distancia))
if distancia < 200:
    print('Caluculado...')
    sleep(1.3)
    print('E o preço da sua passagem será de R${:.2f}'.format(abaixo200))
else:
    print('Calculando...')
    sleep(1.3)
    print('E o preço da sua passagem será de R${:.2f}, pois estamos em promoção'.format(acima200))

preco = distancia * 0.5 if distancia < 200 else distancia * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preco))"""
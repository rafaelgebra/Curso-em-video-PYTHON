v = int(input("Qual a velocidade do carro? "))
l = 80
m = 7
if v >= 80:
    print('Voce passou do limete de velocidade, o valor da multa e {}'.format((v-l)*m))
else:
    print('Parabens voce e um otimo motorista')
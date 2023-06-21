v = int(input("Qual a velocidade do carro? "))
l = 80
m = 7
if v >= 80:
    print('Voce passou do limete de velocidade, o valor da multa e {}'.format((v-l)*m))
else:
    print('Parabens voce e um otimo motorista')



"""velocidade = int(input('Qual a velocidade atual do seu carro? '))
limite = 80
valorMulta = 280
if velocidade >= limite:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    adicional = (velocidade - limite)*7
    if adicional > (velocidade-limite):
        print('O acrescimo por Km/h ultrapasado do limite é de 7 reais o total do acrescimo é de R${}'.format(adicional))
    print('O valor total da multa é R${}'.format(adicional+valorMulta))
print('Tenha um bom dia!')
"""
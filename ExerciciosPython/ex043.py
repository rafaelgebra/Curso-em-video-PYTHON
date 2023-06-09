peso = float(input('Qual o seu peso? '))
alt = float(input('Qual a sua altura '))
imc = peso/(alt ** 2)
if imc < 16:
    print('O seu IMC e de {:.2f} Magreza grau 3'.format(imc))
elif 16 <= imc < 16.9:
    print('O seu IMC e de {:.2f} Magreza grau 2'.format(imc))
elif 17 <= imc < 18.4:
    print('O seu IMC e de {:.2f} Magreza grau 1'.format(imc))
elif 18.5 <= imc < 24.9:
    print('O seu IMC e de {:.2f} Eutrofia'.format(imc))
elif 25 <= imc < 29.9:
    print('O seu IMC e de {:.2f} Sobrepeso'.format(imc))
elif 30 <= imc < 34.9:
    print('O seu IMC e de {:.2f} Obesidade Grau 1'.format(imc))
elif 35 <= imc < 40:
    print('o seu IMC e de {:.2f} Obesidade Grau 2'.format(imc))
elif imc > 40:
    print('O seu IMC e de {:.2f} Obesidade Grau 3'.format(imc))
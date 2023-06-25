n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero '))
if n1 > n2:
    maior = n1
    print(('O numero {} e o maior'.format(maior)))
elif n2 > n1:
    maior = n2
    print('O numero {} e o maior'.format(maior))
elif n2 == n1:
    print('Nao tem valor maior os numeros sao iguais')


"""num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
if num1 > num2:
    maior = num1
    menor = num2
    print('O primeiro valor {} é maior que o segundo valor {}'.format(maior, menor))
elif num2 > num1:
    maior = num2
    menor = num1
    print('O segundo valor {} é maior que o segundo valor {}'.format(maior, menor))
else:
    print('os dois numeros iguais')"""
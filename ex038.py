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

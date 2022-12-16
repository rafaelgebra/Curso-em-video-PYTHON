# Crie um programa que leia dois #
# valores e mostre um menu na tela: #
from time import sleep

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
opcao = 0
while opcao != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos numeros
    [ 5 ] sair do programa''')
    opcao = int(input('Qual a sua opcao '))
    if opcao == 1:
        print('{}'.format(n1 + n2))
    elif opcao == 2:
        print('{}'.format(n1 * n2))
    elif opcao == 3:
        if n1 > n2:
            print('O primeiro numero {} e maior'.format(n1))
        elif n2 > n1:
            print('O segundo numero {} e maior'.format(n2))
    elif opcao == 4:
        n1 = int(input('Digite  novamente o primeiro numero: '))
        n2 = int(input('Digite novamente o primeiro numero: '))
    elif opcao  == 5:
        print('saindo')
        sleep(1)
print('Obrigado por participar')
sleep(2)

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
    print('='*30)
    opcao = int(input('Qual a sua opcao '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma de {} + {} e {}'.format(n1, n2, soma))
    elif opcao == 2:
        multiplicacao = n1 * n2
        print('A multiplicacao de {} * {} e {}'.format(n1, n2, multiplicacao))
    elif opcao == 3:
        if n1 == n2:
            print('Nao tem numero maior ')
        elif n1 > n2:
            maior = n1
            print('Entre {} e {} o maior numero e {}'.format(n1, n2, maior))
        elif n2 > n1:
            maior = n2
            print('Entre {} e {} o maior numero e {}'.format(n1, n2, maior))
    elif opcao == 4:
        n1 = int(input('Digite  novamente o primeiro numero: '))
        n2 = int(input('Digite novamente o primeiro numero: '))
    elif opcao  == 5:
        print('saindo')
        sleep(1)
    else:
        print('opcao invalida. tente novamente.')
        sleep(1)
print('Finalizando... Obrigado por participar')
sleep(2)

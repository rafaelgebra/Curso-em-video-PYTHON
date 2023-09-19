# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: inínio, fim, passo. Seu  programa  tem que realizar três contagens através da função criada:
from time import sleep


def contador(i, f, p):
    """
    -> Sistema de contagem
    :param i: número de início
    :param f: número de fim
    :param p: número do passo
    :return: sem return
    """
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-='*20)
    print(f'Contagem de {i}, até {f}, de {p} em {p}')
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ', flush=True)
            cont += p
            sleep(0.2)
        print('FIM!')
    elif i > f:
        cont = i
        while cont >= f:
            print(f'{cont}',end=' ', flush=True)
            cont -= p
            sleep(0.2)
        print('FIM!')


#programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é dua vez de personalizar o contador')
print('-='*20)
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)


'''
from time import sleep


def contador(i, f, p):
    """
    -> função para contagem de números
    :param i: número do início da contagem
    :param f: número do fim da contagem
    :param p: número do passo da contagem
    :return: sem return
    """
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'A contagem de {i}, até {f}, de {p} em {p}')
    print('-='*20)
    if i < f:
        pos = i
        while pos <= f:
            sleep(0.3)
            print(pos, end=' ', flush=True)
            pos += p
        print('FIM!')
    else:
        pos = i
        while pos >= f:
            sleep(0.3)
            print(pos, end=' ', flush=True)
            pos -= p
        print('FIM!')
    print()


#Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar o contador')
while True:
    inicio = int(input('Início: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))
    contador(inicio, fim, passo)
    while True:
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if continuar in 'SN':
            break
        print('Opção inválida. Digite somente S ou N.')
    if continuar == 'N':
        break
print('Obrigado por participar... Finalizando')
sleep(1)
print('FIM!!')

'''
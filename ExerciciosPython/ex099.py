# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analizar todos os valores e dizer qual dele é o maior.
from time import sleep


def maior(* num):
    print('-='*20)
    print('Analisando os valores passados...')
    c = num_maior = 0
    for valor in num:
        print(f'{valor}', end=' ', flush=True)
        sleep(0.3)
        if c == 0:
            num_maior = valor
        else:
            if valor > num_maior:
                num_maior = valor
        c += 1
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {num_maior}')
    #print(f'O maior valor informado foi {max(num)}' if len(num) > 0 else 'O maior valor informado foi 0') Também da para fazer assim com uma função interna max()



#programa principal
maior(2, 9, 4, 5, 7, 1)   
maior(4, 7, 0)
maior(1, 2) 
maior(6)
maior()

'''
from time import sleep


def maior(*num):
    """
    -> Programa para análise se números
    :param num: é usada a forma de desempacotamento, por isso foi usado o *.
    :return: Sem return.
    """
    sleep(0.2)
    print('-='*20)
    sleep(0.2)
    print('Analisando os valores passados...', flush=True)
    sleep(0.2)
    c = maior_Num = 0
    for valor in num:
        print(valor, end=' ', flush=True)
        sleep(0.2)
        if c == 0:
            maior_Num = valor
        else:
            if valor > maior_Num:
                maior_Num = valor
        c += 1
    sleep(0.2)
    print(f'Foram informados {len(num)} valores ao todo')
    sleep(0.2)
    print(f'O Maior número informado foi {maior_Num}.')
    sleep(0.2)
    print()


def maior2(lis):    # Caso sejá usado uma lista(), NÃO pode por o * indicando que são múltiplos números
    """
    -> Programa para analize de números
    :param lis: é usado uma lista() como parâmetro, por isso não tem *
    :return: Sem return.
    """
    c = maior_Num = 0
    for v in numeros:
        for valor in numeros:
            print(valor, end=' ', flush=True)
            sleep(0.2)
            if c == 0:
                maior_Num = valor
            else:
                if valor > maior_Num:
                    maior_Num = valor
            c += 1
        sleep(0.2)
        print(f'Foram informados {len(numeros)} valores ao todo')
        sleep(0.2)
        print(f'O Maior número informado foi {maior_Num}.')
        sleep(0.2)
        print()
        break


#Programa Principal.
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
numeros = []
for c in range(0, 5):
    numeros.append(int(input(f'Informe o {c+1}º número: ')))
maior2(numeros)

'''
# Crie um programa que tenha função leia_Int(), que vai funcionar de forma semelhante à função input() dp Python, só que fazendo a validação para aceitar apenas um valor númérico.

def leia_Int(msg):
    print('-'*40)
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mErro! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor


#Programa Principal
n = leia_Int('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
"""Crie um progama que leia varios numeros inteiros
pelo teclado. O programa s[o vai parar quando o usuorio
digitar o valor 999, que e a condicao de parada. no final,
mostre quantos numeros foram digitadas e qual foi a
soma entre eles (desconsiderando o flag)"""

n = cont = total = 0
n = int(input('Digite o numero [999 para parar]: '))
while n != 999:
        cont += 1
        total += n
        n = int(input('Digite o numero [999 para parar]: '))
print('Voce digitou {} numeros e a soma entre eles foi {}'.format(cont, total))
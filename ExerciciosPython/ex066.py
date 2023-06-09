"""Crie um programa que leia numeros inteiros pelo teclado.
O programa so vai parar quando o usuario digitar o valor 999,
que e o comando de parada. No final, mostra quantos numeros
foram digitados e qual foi a soma entre elas (desconsidetando o flag)."""

""" Nao precisa por a vareavel 'num' no comeco porque esta com while em loop"""

cont = soma = 0
while True:
    num = int(input('Ditgite um numero (999 para parar): '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'Foram digitados {cont} numeros e a soma e de {soma}')

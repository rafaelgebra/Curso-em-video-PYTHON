# Desenvolva um programa que leia seis #
# numero inteiros e mostres a soma apenas #
# daqueles que forem pares, se o valor digitado #
# for impar, desconsidere-o #
s = 0
co = 0
for c in range(1, 7,):
    n = int(input('Digite o {}o numero. '.format(c)))
    if n % 2 == 0:
        s += c
        co += + 1
print('Voce informou {} numeros pares e a soma foi {}'.format(co, s))

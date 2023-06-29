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

"""
s = 0
c = 0
total = 0
for n in range(1, 7):
    num = int(input('Digite o {}º número inteiro: '. format(n)))
    total += num
    c += 1
    if num % 2 == 0:
        s +=  num

print('A soma de todos os {} números digitados é {} sendo que a soma dos pares é {}'.format(c, total, s))
if s == 0:
    print('Não tem números pares para serem somados.')
"""
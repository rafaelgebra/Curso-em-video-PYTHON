# estruturas de repetição com vareavel de controle #
# Laço,repetições, iteração #

# primeira estrutura de repetição #

''' a estrutura de repeticao + o contador = faco com variavel de controle'''

''' comando de faço 
i = int(input('Inicio. '))
f = int(input('Fim: '))
p = int(input('Passo'))
for c in range(i, f+1, p):
    print(c)
print('FIM')'''

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor '))
    s += n #'''Isso e a mesma coisa que (s = s + n)'''#
print('O somatorio de todos os valores sao {}'.format(s))
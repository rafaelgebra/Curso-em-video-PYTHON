from math import sqrt, ceil, floor
num = int(input('Digite um numero:'))
raiz = sqrt(num)
arr = ceil(raiz)
bai = floor(raiz)
print('A raiz de {} é {:.2f} e arredondada para cima é {} e arredondado para baixo é {}'.format(num, raiz, arr, bai))



#Para arredondar para cima usar assim. porém o valor é inteiro
print('A raiz de {} é {}' .format(num, ceil(raiz)))

#Para arredondar para baixo. poŕem o valor é inteiro
print('A raiz de {} é {} arredondando para baixo é' .format(num, floor(raiz)))
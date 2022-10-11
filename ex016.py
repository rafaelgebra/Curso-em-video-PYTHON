import math
num = float(input('Digite um numero '))
inte = num // 1
print('O numero {} tem a parte inteira {:.0f}'.format(num, inte))
print('O numero {} tem a parte inteira {}'.format(num, math.floor(num)))
print('O numero {} tem a parte inteira {}'.format(num, math.trunc(num)))
print('O numero {} tem a parte inteira {}'.format(num, int(num)))
s = float(input('Qual o salario do funcionario? R$'))
# Nao esta errado porem esta antigo
"""ns = s*10/100
ns2 = s*15/100
if s > 1250:
    print('o novo salario e {}'.format((ns+s)))
if s <= 1250:
    print('O novo salario e {}'. format(ns2+s))"""
if s <= 1250:
    novo = s + (s * 15 / 100)
else:
    novo = s + (s * 10 / 100)
print('Quem recebia o salario de {}{:.2f}{} agora passa a receber o salario no valor de {}{:.2f}{}!!!'.format('\033[31m', s ,'\033[m','\033[32m', novo,'\033[m'))
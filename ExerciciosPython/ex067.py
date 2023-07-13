while True:
    cont = 0
    num = int(input('Quer ver a tabuada de qual numero? '))
    if num >= 0:
        #for cont in range(1, 11): Pode ser feito assim tambem.
        while cont <= 10:
            print(f'{num} x {cont} = {num * cont}')
            cont += 1
    else:
        break
print('Programa de tabuada finalizada. Volte sempre! ')


"""

while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('='*40)
    if num <= -1:
        break
    for c in range(0, 11):
        print(f'{num} X {c:>2} = {num*c}')
    print('='*40)
print('PROGRAMA DE TABUADA ENCERRADA. Volte sempre!!')


"""

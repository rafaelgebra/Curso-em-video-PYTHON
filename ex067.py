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

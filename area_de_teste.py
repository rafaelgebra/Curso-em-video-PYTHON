
while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('='*40)
    if num <= -1:
        break
    for c in range(0, 11):
        print(f'{num} X {c:>2} = {num*c}')
    print('='*40)
print('PROGRAMA DE TABUADA ENCERRADA. Volte sempre!!')
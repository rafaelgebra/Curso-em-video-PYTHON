from time import sleep
def maior(* num):
    print('-='*20)
    print('Analisando os valores passados...')
    c = num_maior = 0
    for valor in num:
        print(f'{valor}', end=' ', flush=True)
        sleep(0.3)
        if c == 0:
            num_maior = valor
        else:
            if valor > num_maior:
                num_maior = valor
        c += 1
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {num_maior}')
    #print(f'O maior valor informado foi {max(num)}' if len(num) > 0 else 'O maior valor informado foi 0') Também da para fazer assim com uma função interna max()



#programa principal
maior(2, 9, 4, 5, 7, 1)   
maior(4, 7, 0)
maior(1, 2) 
maior(6)
maior()
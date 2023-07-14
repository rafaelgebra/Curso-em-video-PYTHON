from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = (input('Par ou Impar? [P/I] ')).upper().strip()[0]
    print(f'Voce jogou {jogador} e o computador jogou {computador}. total de {total}', end=' ')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Voce VENCEU!')
            v +=1
        else:
            print('Voce PERDEU')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Voce VENCEU!')
            v += 1
        else:
            print('Voce PERDEU')
            break
    print('Vamos jogar novamente')
print(f'GAMER OVER! Voce venceu {v} vezes')


"""
from random import randint
print('-='*20)
#print('{:^40}'.format('VAMOS JOGAR PAR OU IMPAR'))
print(f'{"VAMOS JOGAR PAR OU IMPAR":^40}')
print('-='*20)
vitorioa = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    opcao = ' '
    resultado = ' '
    while opcao not in 'PI':
        opcao = str(input('Par ou Impar [P/I]: ')).strip().upper()[0]
    print('-'*40)    
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} {"DEU PAR" if total % 2 == 0 else "DEU IMPAR"}')
    print('-'*40)
    if opcao == 'P':
        if total % 2 == 0:
            resultado = 'PAR'
            vitorioa += 1
            print('Você ganhou!!')

        elif total % 2 == 1:
            resultado = 'IMPAR'
            print('Você perdeu!!')
            break
    elif opcao == 'I':
        if total % 2 == 0:
            resultado = 'PAR'
            print('Você perdeu!!')
            break
        elif total % 2 == 1:
            resultado = 'IMPAR'
            vitorioa += 1
            print('Você ganhou!!')
    print('Vamos jogar novamente...')
print(f'Você conseguiu {vitorioa} vezes. ')    
    


"""
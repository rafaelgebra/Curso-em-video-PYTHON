
jogador = {}
time = []
gols = []

while True:
    total = 0
    jogador['nome'] = str(input('Nome do jogador: ')).strip()
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(0, partidas):
        num = int(input(f'   Quantos gols na partida {c+1}? '))
        gols.append(num)
        total += num
    jogador['gols'] = gols[:]
    jogador['total'] = total
    time.append(jogador.copy())
    gols.clear()
    while True:
        continuar = str(input('Quer continuar? ')).strip().upper()[0]
        if continuar in 'NS':
            break
        print('ERRO! Responda somente SIM ou NÃO')
    if continuar == 'N':
        break
print('-='*30)
print('COD ', end='')
for index in jogador.keys():
    print(f'{index:<15}', end=' ')
print()
print('-'*60)
for keys, value in enumerate(time):
    print(f'{keys:>3}', end=' ')
    for dado in value.values():
        print(f'{str(dado):<15}', end=' ')
    print()

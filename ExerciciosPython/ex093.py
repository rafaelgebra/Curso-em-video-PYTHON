dados = {}
gols = []
total = 0
total2 = 0
dados['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? ' ))
for c in range(0, partidas):
    num = (int(input(f'   Quantos gols na partida {c}: ')))
    gols.append(num)
    total += num
dados['gols'] = gols[:]
dados['total'] = total # ou pode fazer dados['total] = sum[gols]
print('-='*30)
print(dados)
print('-='*30)
for keys, value in dados.items():
    print(f'o campo {keys} tem o valor {value}')
print('-='*30)
print(f'o jogador {dados["nome"]} jogou {partidas} partidas')
for p, g in enumerate(dados['gols']):
    print(f'  => Na partida {p}, fez {gols[p]} gols. ')
    total2 += gols[p]
print(f'Foi um total de {total2} gols')
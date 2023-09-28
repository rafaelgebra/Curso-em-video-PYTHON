#Faça um programa que tenha uma função chamada ficha(), que recebe dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O progama deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(jog='<desconhecido>', gol=0):

    print(f'O jogador {jog} fez {gol} gols no campeonato')
    

#Programa pricipal
n = str(input('Nome do Jogador: ')).capitalize()
g = str(input('número de Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)


'''
def ficha(no='<desconhecido>', gol=0):
    print(f'O Jogador {no}, fez {gol}(s) no campeonato')

#Programa principal
nome = str(input('Nome do Jogador: ')).capitalize().strip()
gols = str(input('Número de Gols: '))

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(gol=gols)
else:
    ficha(nome, gols)

'''
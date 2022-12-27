"""Crie um programa que leia varios numeros inteiros
pelo teclado. No final da execucao, mostre a media
entre todos os valores a qual foi o maor e menor valores lidos
O programa deve perguntar ao usuario se ele quer ou nao continuar
a digitar valores."""
nao = 'S'
cont = total = media = 0
'''while nao in 'Ss' '''
while nao != 'N':
    num = int(input('Digite um numero: '))
    cont += 1
    total += num
    """ foi usado .upper() para deixar todos as letras maiusculas e .strip para retirar os espacos indezejados do comeco e do fim"""
    nao = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
media = total / cont
print('Foram digitados {} o total e {} a media e {}'.format(cont, total, media))
print('O maior valor digitado foi {} e o menor foi {}'.format(maior, menor))



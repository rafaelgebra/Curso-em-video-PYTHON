continuar = ' '
total = maiorv = menorv = contm = valor = 0
barato = ''
while True:
    produto = str(input('Nome do produto: ')).upper().strip()
    valor = int(input('preco: R$'))
    total += valor
    continuar = ' '
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'S':
        maiorv = menorv = valor
    else:
        if valor >= 1000:
            maiorv = valor
            contm += 1
        if valor <= menorv:
            menorv = valor
            barato = produto
    if continuar == 'N':
        break
print(f'O valor total da compra foi R${total} ')
print(f'Temos {contm} produtos custando mais de 1000,00')
print(f'O produto mais barato foi {barato} que custa R${menorv}')

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


"""
print('-'*40)
print(f'{"LOJA SUPER BARATÃO":^40}')
print('-'*40)
total = total_Produto_Caro = menor_Valor = cont = 0
while True:
    continuar = ' '
    produto = str(input('Nome do produto: ')).strip()
    preco = int(input('Preço: R$ '))
    total += preco
    cont += 1
    if cont == 1:
        menor_Valor = preco
        produto_Barato = produto
    else:
        if preco < menor_Valor:
            menor_Valor = preco
            produto_Barato = produto
    if preco >= 1000:
        total_Produto_Caro += 1
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'{"FIM DO PROGRAMA":-^40}')
print(f'O total de compra foi de R${total:.2f}.')
print(f'Temos {total_Produto_Caro} produto custando mais de R$1000,00.')
print(f'O produto mais barato foi {produto_Barato} que custou R${menor_Valor:.2f}.')    

"""
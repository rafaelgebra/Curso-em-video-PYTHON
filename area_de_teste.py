
print('='*20 + 'Loja Guanabara' + '='*20)

preco = float(input('Preço das campas: '))
print('FORMA DE PAGAMENTO')
print('[ 1 ] à vista dinheiro/cheque' )
print('[ 2 ] à vista cartão ')
print('[ 3 ] 2x no cartão ')
print('[ 4 ] 3x ou mais no cartão')
opcao = int(input('Qual é a opção '))
desconto_Avista = (preco * 10) / 100
desconto_Cartao = (preco * 5) / 100
juros = (preco * 20 ) / 100
if opcao == 1:
    print('Sua compra de {} vai custar {} no final com desconto de {} ' .format(preco, preco - desconto_Avista, desconto_Avista))
elif opcao == 2:
    print('')
elif opcao == 3:
    print('')
elif opcao == 4:
    parcelas = int(input('Quantas parcelas '))
    print('Sua compra será parcelar em {}x de R${:.2f}  COM JUROS.' .format(parcelas, juros))
    print('Sua compra de {:.2f} vai custar R${:.2f} no final '.format(preco, preco + juros))
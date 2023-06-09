print('{:=^40}'.format( ' LOJAS GEBRA. KKKK '))
valor = float(input('Quanto voce gastou? '))
print('FORMAS DE PAGAMENTO')
# em vez de colocar varios print pode por no comesso ''' e no fim'''.#
print('[ 1 ] a vista dinheiro/cheque.')
print('[ 2 ] a vista no cartao.')
print('[ 3 ] 2x no cartao.')
print('[ 4 ] 3x ou mais no cartao "COM JUROS".')
# para simpliciar a programa.#
'''pag = int(input('Qual a forma de pagamento? '))
if pag ==1:
    total = valor - (valor*0.1)
elif pag = 2:
    total = valor - (valor*0.05)
elif pag = 3:
    total = valor/2
    print('Sua compra sera parcelada em 2x de R${:.2f}'.format(parcela))
elif pag = 4:
    total = valor + (valor*0.20)
    par = int(input('Qual a quantidade de parcelas? '))
    parcelas = total/par
    print('Sua compra de R${:.2f} vai custar R${:.2f} COM JUROS.'.format(par, parcelas))
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(valor,total))'''
pag = int(input('Qual a forma de pagamento? '))
if pag == 1:
    print('Pagamento a VISTA no dinheiro ou chegue tem desconto de 10% que e R${:.2f} entao o valor total R${:.2f}'.format(valor * 0.1, valor-(valor*0.1)))
elif pag == 2:
    print('Pagamento a VISTA no cartao tem desconto de 5% que da R${:.2f} entao o valor total e de R${:.2f}'.format(valor * 0.05, (valor-(valor*0.05))))
elif pag == 3:
    print('Pagamento em ate 2x no cartao nao tem juros, o valor total do produto e R${:.2f} com parcelas de R${:.2f}.'.format(valor, valor/2))
elif pag == 4:
    par = int(input('Qual a quantidade de parcelas? '))
    if par == 3:
        print('Pagamento no cartao em 3x ou mais tem 20% juros. O valor da parcela e de R${:.2f}. E o valor total e de R${:.2f}.'.format(((valor*0.20)+valor/par), (valor*0.20)+valor))
    elif par == 4:
        print('Pagamento no cartao em 3x ou mais tem 20% juros. O valor da parcela e de R${:.2f}. E o valor total e de R${:.2f}.'.format(((valor*0.20)+valor/par), (valor*0.20)+valor))
    elif par == 5:
        print('Pagamento no cartao em 3x ou mais tem 20% juros. O valor da parcela e de R${:.2f}. E o valor total e de R${:.2f}.'.format(((valor*0.20)+valor/par), (valor*0.20)+valor))
    elif par == 6:
        print('Pagamento no cartao em 3x ou mais tem 20% juros. O valor da parcela e de R${:.2f}. E o valor total e de R${:.2f}.'.format(((valor*0.20)+valor/par), (valor*0.20)+valor))
    elif par == 7:
        print('Pagamento no cartao em 3x ou mais tem 20% juros. O valor da parcela e de R${:.2f}. E o valor total e de R${:.2f}.'.format(((valor*0.20)+valor/par), (valor*0.20)+valor))
    elif par == 8:
        print('Pagamento no cartao em 3x ou mais tem 20% juros. O valor da parcela e de R${:.2f}. E o valor total e de R${:.2f}.'.format(((valor*0.20)+valor/par), (valor*0.20)+valor))
    elif par == 9:
        print('Pagamento no cartao em 3x ou mais tem 20% juros. O valor da parcela e de R${:.2f}. E o valor total e de R${:.2f}.'.format(((valor*0.20)+valor/par), (valor*0.20)+valor))
    elif par == 10:
        print('Pagamento no cartao em 3x ou mais tem 20% juros. O valor da parcela e de R${:.2f}. E o valor total e de R${:.2f}.'.format(((valor*0.20)+valor/par), (valor*0.20)+valor))
    else:
        print('Opecao invalida. Tente novamente!')
else:
    print('Opecao invalida. Tente novamente!')
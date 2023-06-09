casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o valor do seu salario? R$'))
anos = int(input('Quantos anos voce vai pagar? '))
meses = anos*12
vtotal = (salario*30/100)*meses
vparcela = casa/meses

if vtotal >= casa:
    print('Parabens voce conseguiu o financiamento o valor sera de {:.2f} por mes e sera pago em {:.2f} parcelar'. format(vparcela, meses))
else:
    print('Infelizmente voce nao foi aprovado')



salario = float(input('Qual o seu salário? '))
if salario < 1250:
    novo = salario + (salario * 0.15) #(salario * 15 / 100)
if salario > 1250:
    novo = salario + (salario*0.10) # (salario * 10 / 100)
print('O salario de quem recebe {} agora vai ser {}'.format(salario, novo))
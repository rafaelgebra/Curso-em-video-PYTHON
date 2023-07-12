resposta = 'S'
maior = menor = cont = soma = 0
while resposta != 'N': # também da para fazer assim = while resposta in 'Nn':
    num = int(input('Digite um número: '))
    resposta = str(input('Quer continuar? [S/N]: ')).strip().upper()
    cont += 1
    soma += num
    if cont == 1 :
        maior = num
        menor = num 
    else:    
        if maior < num:
            maior = num
        if menor > num:
            menor = num
print('você digitou {} e a média foi de {:.2f} \n O maior valor foi {} e o menor foi {}' .format(cont, (soma/cont), maior, menor))

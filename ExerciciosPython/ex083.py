expr = str(input('Digite expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão esta valida')
else:
    print('Sua expressao esta errada')


"""
expr = str(input('Digite uma expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está correta! ')
else:
    print('Sua expressão está errada! ')

    
    EX: 2
    
expressao = str(input('Digite uma expressão: '))
pilha = []
for simbulo in expressao: 
    if simbulo == '(':
        pilha.append(simbulo) # pilha.append('(')
    elif simbulo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(simbulo) #pilha.simbulo(')')
            break
if len(pilha) == 0:
    print('Sua expressão esta valida')
else:
    print('Sua expressao esta errada')

    
    EX: 2



    dados = list()
temp = list()
peso_Maior = peso_Menor = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))

    if len(dados) == 0:
        peso_Maior = peso_Menor = temp[1]
    else:
        if temp[1] > peso_Maior:
            peso_Maior = temp[1]
        if temp[1] < peso_Menor:
            peso_Menor = temp[1]
    dados.append(temp[:])
    temp.clear()
    continuar = ' '
    while continuar not in 'NnSs':
        continuar = str(input('Quer continuar? '))
    if continuar in 'Nn':
        break
print(dados)
print(f'Ao todo você cadastrou {len(dados)}')
print(f'O maior peso foi de {peso_Maior}. Peso de', end=' ')
for pessoa in dados:
    if pessoa[1] == peso_Maior:
        print(f'{pessoa[0]}', end=', ')
print()
print(f'O menor peso foi de {peso_Menor}. Peso de', end= ' ')
for pessoa in dados:
    if pessoa[1] == peso_Menor:
        print(f'{pessoa[0]}', end=', ')
print()


"""
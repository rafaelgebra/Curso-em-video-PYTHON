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



"""
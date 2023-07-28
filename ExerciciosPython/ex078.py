lista = []
menor = maior = 0
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posicao {c}: ')))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]
 #eu fiz assim...   maior = max(lista) #o maior valor dentro da lista/tupla pode ser encontrado assim max(lista)
 #eu fiz assim...   menor = min(lista) #o menor valor dentro da lista/tupla pode ser encontrado assim min(lista)
print(f'Voce digitou os numeros {lista}')
print(f'O maior valor digitado foi {maior} nas posicoes ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi {menor} nas posicoes ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}... ', end='')
print()



"""

valores = []
menor = maior = 0
for c in range(0, 5):
    valores.append(int(input(f'Digite o valor para a Posição {c}: ')))
    if c == 0:
        menor = maior = valores[c]
        #posicao_Maior = posicao_Menor = v - Para ter a posição do primeiro valor
    else:
        if valores[c] < menor:
            menor = valores[c]
            #posicao_Menor = v - Para ter a posição do primeiro valor
        elif valores[c] > maior:
            maior = valores[c]
            #posicao_Maior = v - Para ter a posição do primeiro valor
print('-'*60)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {maior} na posição ', end='')
for i, v in enumerate(valores):
    #print(f'i {i}')
    #print(f'v {v}')
    if valores[i] == maior:
        print(f'{i}...', end='')
print(f'\nO menor valor digitado foi {menor} na posição ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...')
print()


#


lista = []
maior = menor = 0
for c in range(0, 5):
    lista.append(int(input(f'Digite um valore para a posição {c}: ')))
for i, numero in enumerate(lista):  #           SEM a função FOR
    if i == 0:                      #   if c == 0 
        maior = menor = numero      #       maior = menor = lista[c]
    else:                           #   else:
        if numero > maior:          #       if lista[c] > maior:
            maior = numero          #           maior = lista[c]
        elif numero < menor:        #       elif lista[c] < menor:
            menor = numero          #           menor = lista[c]
print('-'*30)
print(f'Você digitou os valores {lista}')
print('-'*30)
print(f'O maior valor digitado foi {maior} na posição ', end='')
for p, v  in enumerate(lista):
    if v == maior:
        print(f'{p}...', end='')
print()
print(f'O menor valor difitado foi {menor} na posição ', end='')
for p , v in enumerate(lista):
    if v == menor:
        print(f'{p}...', end='')
print()


"""
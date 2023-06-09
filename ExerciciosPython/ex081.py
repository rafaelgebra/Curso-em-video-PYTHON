lista = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    r = str(input('Você quer continuar? [S/N]')).upper()[0]
    if r in 'Nn':
        break
if 5 in lista:
    cinco = 'faz parte da lista'
else:
    cinco = 'não faz parte de lista'
print('-='*30)
print(f'Você digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ondem decrescente são {lista}')
print(f'O valor 5 {cinco}')

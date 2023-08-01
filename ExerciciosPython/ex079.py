num = list() #O nome da minha lista é num
while True: # Lupe infinito
    n = (int(input('Digite um valor: ')))# input de adicionamento de numero na lista
    if n not in num:
        num.append(n)
        print('Adicionado com sucesso...')
    else:
        print('Valor duplicado! Tente outro número')
    continuar = str(input('Quer continuar [S/N]: ')).upper()[0]# input de pergunta se quer ou não continuar o programa
    if continuar in 'Nn': # teste logico se vai sair do programa ou continuar
        break
num.sort()
print(num)


"""
lista_Num = []

while True:
    num = (int(input('Digite um valor: ')))
    if num not in lista_Num:
        lista_Num.append(num)
        print('Valor adinionado com sucesso')
    else:
        print('Valor duplicado. Não vou adicionar!!')
    continuar = ' '
    while continuar not in 'SsNn':
        continuar = str(input('Quer continuar? [S/N]: ')).strip()
    if continuar in 'Nn':
        break

print('-'*60)
lista_Num.sort()
print(f'Você digitou os valores {lista_Num}') 
print('-'*60)
lista_Num.sort(reverse=True)
print(f'Os números ao contrario {lista_Num}')



Refeito 



valores = []
while True:
    num = int(input('Digite um valor: '))
    if num in valores:
        print('Valor duplicado não vou adicionar.')
    else:
        valores.append(num)
        print('Valor adicionado com sucesso')
    continuar = ' '
    while continuar not in 'NnSs':
        continuar = str(input('Quer continuar? [S/N] ')).strip()
    if continuar in 'Nn':
        break
valores.sort()
print(valores)



"""



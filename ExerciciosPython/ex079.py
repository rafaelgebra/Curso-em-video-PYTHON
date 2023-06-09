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



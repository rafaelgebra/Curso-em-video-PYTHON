tabela = list()
for c in range(0, 5):
    n = int(input('Digite um número: '))
    if c == 0 or n > tabela[-1]:
        tabela.append(n)
        print('Adicinado ao final da tabela')
    else:
        pos = 0
        while pos < len(tabela):
            if n <= tabela[pos]:
                tabela.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista... ')
                break
            pos +=1
print(f'Os valores digitados em ordem foram{tabela} ')


"""
lista_Valores = []
for c in range(0,8):
    num = (int(input('Digite um Valor: '))) 
    if num not in lista_Valores: # Verifica se o número já esta na lista -  Caso não esteja continua
        if c == 0 or num > lista_Valores[-1]: # também pode ser escrito assim # if c == 0 : 
            lista_Valores.append(num)                                         #     lista_Valores.append(num)
            print('Valor adicionado ao final da lista...')                            # elif n > lista_Valores[-1] # ou n > lista[len(lista)-1]: 
                                                                              #     lista_Valores.append(num)
        else:
            pos = 0
            while pos < len(lista_Valores): # Verifica em qual posição vai ser adicionado o valor
                if num <= lista_Valores[pos]:
                    lista_Valores.insert(pos, num)
                    print(f'Adicionado na posição {pos} da lista...')
                    break
                pos += 1
    else: # Verifica se o número já esta na lista - Caso ja tenha o número da um aviso que não vai adicionar
        print('Valor já adicionado, não vou adicionar novamente!!')
print('-'*60)
print(f'Os valores digitados em ordem crescente foram {lista_Valores}')

lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[len(lista)-1]:
        lista.append(n)
        print('Adicionado na ao final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista')
                break
            pos += 1
print(f'Os valores digitados em ordem foram {lista}')






"""
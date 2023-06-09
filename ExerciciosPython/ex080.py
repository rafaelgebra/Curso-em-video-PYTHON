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
print(f'Os valores digitados em ondem foram{tabela} ')
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
mais_Termos = 10
total = 0
while mais_Termos != 0:
    total += mais_Termos
    while cont <= total:
        print('{} -> ' .format(termo), end=' ')
        termo += razao
        cont += 1
    print('PAUSA')
    mais_Termos = int(input('Quantos termos você quer mostrar a mais? '))
    
print('A quantidade de termos são {} ' .format(cont))
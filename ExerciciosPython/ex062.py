"""Melhore o DESAFIO 61, perguntando para o usuario se ele
quer mostrar mais alguns termos, O programa encerrara quando
ele quisser que quer mostrar termos"""

print('-='*20)
primeiro = int(input('Primeiro termo : '))
razao = int(input('Razao : '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{}'.format(termo), end='-> ')
        termo += razao
        cont += 1
    mais = int(input('\nQuantos termos voce quer ver a mais '))
print('Processo finalizado com sucesso com {} termos mostrados'.format(total))


"""
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

"""
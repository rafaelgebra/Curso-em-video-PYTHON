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
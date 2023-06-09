# Aula 15 - Interrompendo repeticoes while
'''Laco de repeticao parte 3 '''

"""novas fstrings/ para apartir do Python 3.6"""

'''nessa aula esta sendo estado a função (break) ela é usada para interomper
um loop, mas também pode ser usada em muitas coisas.
Por exemplo.
parar uma contagem/soma a utilizacao dela depende da criatividade'''

n = s = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    s += n
print('A soma vale {}'.format(s))
print(f'Soma vale {s}')


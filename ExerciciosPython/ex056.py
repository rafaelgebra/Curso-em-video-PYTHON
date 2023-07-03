somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = 0
totmulher20 = 0

contf = 0
contm = 0
for grup in range(1, 5):
    nome = str(input('Qual o nome? ')).upper().strip()
    idade = int(input('Qual o seu idade? '))
    sexo = str(input('Qual o seu sexo [M/F]? ')).upper().strip()
    somaidade += idade
    if grup ==1 and sexo in 'Mn':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mn' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print('A media de idade do grupo e de {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem,nomevelho ))
print('Ao todo sao {} mulheres com menos de 20 anos'.format(totmulher20))

"""

soma_Idade = 0
media_Idade = 0
maior_Idade_M = 0
nome_M_Velho = ''
total_F_20 = 0

for pessoas in range(1, 5):
    print('{:-^30} '.format(' {}º PESSOA ') .format(pessoas))
    nome = str(input('Qual o seu nome? ')).strip()
    idade = int(input('Qual a sua idade? '))
    sexo = str(input('Qual o seu sexo? [M/F]: ')).strip()
    media_Idade += idade
    if pessoas == 1 and sexo in 'Mm':
        maior_Idade_M = idade
        nome_M_Velho = nome
    if sexo in 'Mm' and idade > maior_Idade_M:
        maior_Idade_M = idade
        nome_M_Velho = nome
    if sexo in 'Ff' and idade < 20:
        total_F_20 += 1


print('A média de idade do grupo é de {} anos'. format(media_Idade / 4))
print('O homem mais velho tem {} e seu nome é {} ' .format(maior_Idade_M, nome_M_Velho))
print(' O total de mulheres a baixo de 20 anos é {}' .format(total_F_20))
"""
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
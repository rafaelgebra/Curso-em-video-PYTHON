nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
media = (nota1 + nota2)/2
if 5 >= media:
    media = 'Reprovado'
elif (5 < media) and (6.9 > media):
    media = 'Recuperacao'
elif (6.9 <= media) and (10 >= media):
    media = 'Aprovado'
else:
    print('Erro digite as notas novamente')
print(media)

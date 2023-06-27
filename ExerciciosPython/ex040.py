nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
media = (nota1 + nota2)/2
if 5 >= media:
    print('A sua primeira nota e {} e a sua segunda nota e {} e a sua media e {} entao voce esta '.format(nota1, nota2, media))
    media = 'Reprovado'
elif (5 < media) and (6.9 > media):
    media = 'Recuperacao'
elif (6.9 <= media) and (10 >= media):
    media = 'Aprovado'
else:
    print('Erro digite as notas novamente')
print(media)


"""
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print('Quem tirou {} e {}, a média do aluno é {:.1}' .format(nota1, nota2, media))
if media >= 7:
    print('O aluno está APROVADO')
elif 7 < media >= 5 :
    print('Aluno em RECUPERAÇÃO.')
elif media < 5:
    print('Aluno REPROVADO.')
"""
nome = str(input('Qual o seu nome? ')).strip()
print('Analizando o seu nome.')
print('O seu nome em maiuscolo e {}'.format(nome.upper()))
print('O seu nome em minuscolo e {}'. format(nome.lower()))
print('O seu nome tem ao todo {} letras SEM espaço'.format(len(nome) - nome.count(' ')))
print('O primeiro nome tem {} letras '.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome e {} e ele tem {} letras'. format(separa[0], len(separa[0])))
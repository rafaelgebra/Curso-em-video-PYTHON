                'Aula 9'

'''Fratiamento de string'''

frase = 'Curso em Video Python'
print(frase[9]) -> 'Significa que o python vai pegar o caracter 9'
print(frase[:15] -> )
print(frase[9:15] -> 'Significa que é pra pegar do caracter 9 até o 14, não pega a o ultimo porque o python o ultimo é excluido ')
print(frase[9:21] -> 'Nessa frase o caracter 21 nao existe. ate da para usar porque esta um caracter acimada maxima, mas nao a melhor forma de utilizar.')
print(frase[9:21:2] -> 'começa no 9 caracter e vai até o 21 caracter porem saltando de 2 em 2')
print(frase[:5] -> 'quando nao tem o caracter inicial vai ate o caracter 5')
print(frase[15:] -> 'Significa que sabe ainde comeca a contar os caracter mas nao tem a indicacao do fim da string entao vai ate o sim dela, "nesse casa tem a palavra 'PYTHON'"')
print(frase[9::3]) -> 'Comeca no 9 e vai ate o fim, porem tem o :3 que siguinifica pular de 3 em 3'

'''analise'''
'Analisa uma string e muito importante, tamanho, qual letra comeca ou termina...'
print(len(frase)) #len significa comprimento#
print(frase.count('o')) #count significa contar#
print(frase.count('o',0,13)) #o puthon ja faz uma contagem com fatiamento#
print(frase.find('deo')) #find significa encontrar # -> find mostra aonde comecou a procura
print(frase.find('Android')) -> 'Quando a streng nao existe ou nao encontrado o python retorna -1'
print('Curso' in frase) ->  'in significa, em ou tem' '{se tem a palavra o python retorna TRUE}' "in nao e uma funcao e um operador mas da para fazer analize"

''' Transformacao'''
"""Uma lista de string e imutavel, ms consegue mexer com os metodos"""
print(frase.replace('Python','Android')) # replace significa trocar/reposicionar
print(frase.upper()) # tudo maiuscolo e obrigatorio os () no final
print(frase.lower())   # tudo minisculo e obrigatorio os () no final
print(frase.capitalize()) # so a primeira letra maiuscolo, e obrigatorio no final ()
print(frase.title()) # a primeira letra da palavra fica maiusculo(consegue fazer isso pela posicao dos espacos, e obrigatorio no final ()
print(frase.strip()) # remove todos os espacos inuteis no fim e no comeco
print(frase.rstrip()) # remove somente os ultimos espacos (lado da direita)
print(frase.lstrip()) # remove somente os primeros especas (lado esquerdo)

'''Divisao'''
print(frase.split()) # por padrao uma divicao entro da str considerando os espacos
        'Curso em Video Python'
        '01234 01 01234 012345'

'''Juncao'''
print('-'.join(frase))
        'Curso em Video Python'
        '01234 01 01234 012345'
'com join (juntar) consegue juntar uma coisa na outro, no caso de ("Curso em Video Python" vira uma str unica "Curso-em-Video-Python" porque foi selecionado - no lugar de espaco)'


frase2 = '   Aprenda Python  '
print(frase2)
print(frase2.strip()) # remove os espacos da direota e esquerda
print(frase2.rstrip()) # remove os espacos da direita
print(frase2.lstrip()) # remoce os espacos da esquerda
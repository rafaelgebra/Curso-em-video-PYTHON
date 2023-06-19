frase = str(input('Escreva uma frase ')).strip().upper()
print("Nesta frase tem {} A".format(frase.count('A')))
print('A posicao do primeiro A esta em {} '.format(frase.find('A')+1)) # O +1 é para facilitar para o usuario a posição mas para o python é posição 0 
print('A posicao da ultima letra A esta em {}'.format(frase.rfind('A')+1))# O +1 é para facilitar para o usuario a posição mas para o python é a primeira posição da direita para a esquerda 
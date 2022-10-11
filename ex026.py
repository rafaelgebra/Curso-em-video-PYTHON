frase = str(input('Escreva uma frase ')).strip().upper()
print("Nesta frase tem {} A".format(frase.count('A')))
print('A posicao do primeiro A esta em {} '.format(frase.find('A')+1))
print('A posicao da ultima letra A esta em {}'.format(frase.rfind('A')+1))
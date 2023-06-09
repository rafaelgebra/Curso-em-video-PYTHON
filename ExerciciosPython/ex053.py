frase = str(input('Escreva uma palavra ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]

''' inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
# essas linhas de comando podem ser resulmidas no python
por uma variavel e usando o fatiamento (inverso = junto::-1]'''

print('O inverso de {} e {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um PALINDROMO!')
else:
    print('A frase digitada nao e um PALINDROMO')
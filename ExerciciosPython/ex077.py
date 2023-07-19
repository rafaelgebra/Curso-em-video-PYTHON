palavras = ('aprender', 'programar',
          'linguaguem', 'python',
          'curso', 'gratis',
          'estudar', 'pratica',
          'trabalhar', 'mercado'
          'programador', 'futuro')
for p in palavras: # quando se usa o for nessa linha esta indicando que é para repetir até a última palavra da tupla.
    print(f'\nNa pafavra {p.upper()} temos ', end='') # indicando que vai imprimir a tupla formatada por e o que vai imprimi é uma posição ta tupla de cada vez
    for letra in p: #com o for aninhado a outro for, pode indicar que a repetição "letra" vai ser feita separadamente/analizada uma palavra de cada vez
        if letra.lower() in'aeiou': #com esse if faz o teste logico com as vogais, e deixa imprimir só as vogais
                print(letra, end=' ')

"""

lista = ('APRENDER','PROGRAMAR','LINGUAGEM')

Ex:1

for elemento in lista:
    print(f'\nNa palavra {elemento.upper()} tem', end=' ')
    for letra in elemento:
        if letra in 'AEIOU':
            print(letra.lower(), end=', ')
print(f'\n{"FIM":-^40}')


Ex:2
for palavra in lista:
    print(f'\nNa palavra {palavra.upper()} temos', end=' ')
    for letra in palavra:
        if letra in 'AEIOU':
            print(f'{letra.lower()}', end=' ')
print('\n')


"""
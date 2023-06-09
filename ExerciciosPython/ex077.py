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

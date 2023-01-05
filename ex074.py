from random import randint
numeros = (randint(0, 10), randint(0, 10), randint(0, 10),
             randint(0, 10), randint(0, 10), )
print(f'Os valores sorteados foram {numeros}')
print(f'O maior numero é {max(numeros)}')
print(f'O menor numero é {min(numeros)}')

frase = 'Curso em Vídeo Python'
print(frase.upper().count('O'))
print(len(frase.strip()))
print(frase.replace('Python', 'Android'))
print(frase)
print('Curso' in frase)
print(frase.find('Curso'))
print(frase.lower().find('vídeo'))

dividido = frase.split() # transforma em uma lista
print(dividido) #['Curso', 'em', 'Vídeo', 'Python' / transforma cada palavra em um índice separado
print(dividido[0]) # Curso / foi celecionado o itém 0 da lista
print(dividido[2][3]) # e / foi celecionado o a letra referente ao índece 3 do itém 2 da lista
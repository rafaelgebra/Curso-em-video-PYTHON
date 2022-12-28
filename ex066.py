"""Crie um"""


cont = soma = 0
while True:
    num = int(input('Ditgite um numero (999 para parar): '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'Foram digitados {cont} numeros e a soma e de {soma}')

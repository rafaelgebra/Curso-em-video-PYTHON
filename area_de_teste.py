cont = soma = 0
while True:
    num = int(input('Digiete um valor [999 pra parar]: '))
    if num == 999:
        break
    soma += num
    cont += 1
print(f'A soma dos {cont} valores foi de {soma:.2f}')
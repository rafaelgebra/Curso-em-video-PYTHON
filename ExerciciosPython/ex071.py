<<<<<<< HEAD

v1 = int(input('Primeiro '))
v2 = int(input('Segundo '))
print(v1 + v2 )
=======
valor = int(input('Qual o valor que você quer sacar? R$ '))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break

=======
v1 = int(input('Primeiro '))
v2 = int(input('Segundo '))
print(v1 + v2 )
>>>>>>> f9169c674ae7976ea77affd838a9f1c29368bbc6

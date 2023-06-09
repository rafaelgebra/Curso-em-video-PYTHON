print('-='*20)
print('-=-=-=-=-=-= Analizador de triangulos -=-=-=-=-=-=-')
print('-='*20)
print()
r1 = float(input('Digite o primeiro segmento: '))
r2 = float(input('Digite o segundo segmento: '))
r3 = float(input('Digiete o terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimento acima \033[;30;41mPODEM FORMAR\033[m um triangulo')
else:
    print('Os seguimento acima \033[;30;43mNAO PODEM\033[m um triangulo')

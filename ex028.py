import random
print('Tente descobrir o numero que eu "PENSEI"')
n1 = int(input('Digite um numero: '))
n2 = random.randint(1,5)
if n1 == n2:
    print('Voce venceu')
else:
    print('voce perdeu o numero correto e {}'.format(n2))
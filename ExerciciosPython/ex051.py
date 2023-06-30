primeiro = int(input('Primeiro termo "NUMERO" '))
razao = int(input('Razao "PULAR" '))
decimo = primeiro + (10-1) * razao
for c in range(primeiro, decimo + razao, razao):
    print('{}'.format(c), end='-> ')
print('FIM')

"""
print('='*30)
print('{:^30}'.format(' 10 TERMOS DE UMA PA '))
print('='*30)
termo = int(input('Digite o termo: '))
razao = int(input('Digite a razão: '))
dec = termo + (10 - 1) * razao # formula de uma PA
for c in range(termo, dec + 1, razao): # 0 +1 é para ter o decimo termo
    s = termo + razao + razao
    print(c, end=' -> ')
print('acabo')
"""

s = 0
c = 0
total = 0
for n in range(1, 7):
    num = int(input('Digite o {}º número inteiro: '. format(n)))
    total += num
    c += 1
    if num % 2 == 0:
        s +=  num

print('A soma de todos os {} números digitados é {} sendo que a soma dos pares é {}'.format(c, total, s))
if s == 0:
    print('Não tem números pares para serem somados.')
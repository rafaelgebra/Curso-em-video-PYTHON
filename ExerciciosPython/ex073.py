listacom = ('Palmeiras', 'Internacional', 'Fluminense',
            'Corinthians', 'Flamengo','Athetico Paranaense',
            'Alhético Mineiro','Fortaleza','São Paulo', 'América Fc Sat',
            'Botafogo','Santos','Goiás','Red Bull Bragantino', 'Coritiba',
            'Cuiabá Sat', 'Ceará', 'Atletico', 'Avaí', 'Juventude')
#for t in listacom: # formatado de forma organizada.
#    print(t)
print('-=' * 20)
print(f'Lista de times do Brasileirão: {listacom}')
print('-=' * 20)
print(f'Os 5 primeiros são {listacom[:5]}')
print('-=' * 20)
print(f'Os 4 últimos são: {listacom[-4:]}')
print('-=' * 20)
print(f'Time em ordem alfabética: {sorted(listacom)}')
print('-=' * 20)
print(f'Qual a posição do São Paulo {[listacom.index("São Paulo")+1]}')
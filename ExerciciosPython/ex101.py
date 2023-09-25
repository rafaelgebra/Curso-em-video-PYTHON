# Atividade 1 com docstring
#Crie um programa que tenha uma função chamada voto() que vai receber como parametro o ano de nascimento de uma pessoa. retornando um valor literal indicando se uma pessoa tem voto, NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições
def voto(ano):
    """
    atual: é a data do dia
    idade: idade de uma pessoa
    if: comparação se é melhor de 16 anos
    elif: comparação se é voto opcional 16 e 17 anos ou maior que 65 anos de idade
    elif: comparação se o voto é obrigatorio 
    """
    from datetime import date
    atual = date.today().year
    idade = atual - nasc
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade <= 17 or idade > 65:
        return f'COM {idade} anos: VOTO OPCIONAL'
    elif idade <= 64:
        return f'Com {idade} anos: VOTO OBRIGATORIO.'


#Programa Principal
nasc = int(input('Em que ano você nasceu? '))    
print(voto(nasc))


# Atividade 2 sem docstring
"""
def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATORIO.'


#Programa Principal    
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
"""
'''
def voto():
    """
    -> Programa para definir se o voto é obrigatório
    :return: Sem return
    """
    from datetime import date
    atual = date.today().year
    nasc = int(input('Digite o seu ano de nascimento: '))
    idade = atual - nasc
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA'
    elif 16 <= idade < 18 or idade >= 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    elif 18 <= idade < 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'


#Programa Principal
print(voto())


'''
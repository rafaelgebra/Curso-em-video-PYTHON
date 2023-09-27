#Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
# - Quantidade de notas.
# - A maior nota.
# - A menor nota.
# - A média da turma.
# - A situação (opcional).
# Adicione também as dacstring.

import math

def notas(*n, sit=False):
    """
    -> Função para analizar notas e situação de vários alunos
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com váriasinformações sobre a situação da torma.
    """
    r = {}
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = math.ceil(sum(n)/len(n)) # A biblioteca MATH foi baixada para usar a função arredondamento para cima.
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r

#Programa Principal
resp = notas(5.5, 2.5, 9, 8.5, sit=True)
print(resp)


'''
def aluno():
    """
    -> Função que adiciona notas ao nome do aluno
    :return: Sem return
    """
    notas = []
    classe['aluno'] = str(input('Nome do aluno: ')).capitalize()
    while True:
        nota = str(input(f'nota do aluno {classe["aluno"]}: [999] interrompe o programa '))
        if nota.isnumeric():
            valor = int(nota)
            if valor == 999:
                break
            notas.append(valor)
        else:
            print('\033[0;31mErro! Digite um valor válido.\033[m')
    classe['notas'] = notas[:]
    notas.clear()


def notasA(*num, sit=True):
    """
    -> Função de analize das notas do aluno
    :param num: Parámetro que vem da função classe()
    :param sit: Mostrar ou não a situação do aluno (opcional)
    :return: Retorna os dados dentro do dicionaria aluno{}
    """
    total = 0
    aluno = {}
    aluno['nome'] = classe['aluno']
    aluno['total'] = len(classe['notas'])
    aluno['maior'] = max(classe['notas'])
    aluno['menor'] = min(classe['notas'])
    for valor in classe['notas']:
        total += valor
    aluno['média'] = total / aluno['total']
    if sit:
        if aluno['média'] < 5:
            aluno['situação'] = 'ruim'
            return aluno
        elif 5 < aluno['média'] < 7:
            aluno['situação'] = 'boa'
            return aluno
        elif 7 <= aluno['média'] <= 10:
            aluno['situação'] = 'ótimo'
            return aluno
    else:
        return aluno


#Programa Principal
classe = {}
res = notasA(aluno(), sit=True)
print(res)

'''
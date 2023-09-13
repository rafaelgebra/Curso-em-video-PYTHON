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
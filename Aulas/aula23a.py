try: # tentar
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b
#except Exception as erro:
    print(f'problema encontrado foi{erro.__class__}') # Dessa maneira podemos mostra de forma personalizar o erro
#except TypeError: # se der erro/problema | o TypeError é especificando o erro/problema
    'Falha'
#except ValueError: # Se der erro/problema | o ValurError mostra o valor do erro/problema
    'Falha'
except ZeroDivisionError: # Se der erro/problema | O ZeroDivisionError mostra que a "conta" não é dividido por 0
    print('Não é possivel dividir um número por ZERO (0)')
except KeyboardInterrupt:
    print('Usúario preferio não informar os dados')
except (ValueError, TypeError, ZeroDivisionError): # Podemos por mais de uma ecessão no mesmo except
    print('Tivemos problemas com os tipos de dados que você digitou')
except: # excessão generica.
    print('tivemos um problema')
else:#Opcional # Se o comando deu certo mais teve um ptoblema com o resultado mostra qual é
    print(f'O resultado é {r}')
finally:#Opcional # acontece independete se del falha ou não, o que "Escrever aqui vai aparecer"
    print('Volte sempre! Muito obrigado!')

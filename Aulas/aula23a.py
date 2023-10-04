try:
    'Operação'
except TypeError:
    'Falha'
except ValueError:
    'Falha'
except ZeroDivisionError:
    'Falha'
else:#Opcional
    'Deu certo'
finally:#Opcional
    'Certo/falha'
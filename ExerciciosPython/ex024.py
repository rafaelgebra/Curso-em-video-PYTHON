ci = str(input('Que cidade voce nasceu ')).strip()

print('A cidade que voce digitou é {} e ela começa com {} '.format(ci, ci[:5].upper() == 'SANTO'))

sexo = str(input('Informe o eu seu SEXO: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('SEXO {} registrado com sucesso'.format(sexo))
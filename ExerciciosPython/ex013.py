nom = input('Qual o nome do funcionario? ')
sal = float(input('Qual o salario do funcionario? R$'))
nov = sal*0.15
print('O novo salario do funcionario {} e {:.2f}'.format(nom, (sal+nov)))
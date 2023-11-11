from time import sleep
from lib.interface import *
from lib.arquivos import *

arq = 'cursoemvideo.txt'

if not arquivo_Existe(arq):
    criar_Arquivo(arq)

while True:
    resposta = menu(['Ver pessas cadastrada', 'Cadastrar nova Pessoa', 'Excluir pessoa cadastrada', 'Sair do Sistema'])
    if resposta == 1:
        #Opçãp de listar o conteúdo do arquivo!
        ler_Arquivo(arq)
    elif resposta == 2:
        #Opção de cadastrar uma nova pessoa.
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leia_Int('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('EXCLUIR CADASTRO')
        excluir(arq)
    elif resposta == 4:
        # Opção de sair do sistema.
        cabecalho('Saindo do Sistema... até logo!')
        sleep(1)
        break
    else:
        #Digitou uma opção errada no menu.
        print('\033[31mERRO! Opção invalida!\033[m')
    sleep(1)
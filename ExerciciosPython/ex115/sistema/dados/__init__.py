def leia_Int(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsúario interrompeu o programa\033[m')
            return 0
        else:
            return num


def linha(tam=42):
    return '=' * 42


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho(f'{"MENU PRINCIPAL"}')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    while True:
        opc = leia_Int('\033[33mSua opção: \033[m')
        if opc == 1:
            pessoas(opc)
        elif opc == 2:
            cadastro(opc)
        elif opc == 3:
            sair(opc)
            break
        else:
            print('\033[31mERRO: por favor, digite um número válido\033[m')


def pessoas(num):
    cabecalho(f'{f"OPÇÃO {num}"}')


def cadastro(num):
    cabecalho(f'{f"OPÇÃO {num}"}')


def sair(num):
    cabecalho(f'{"Saindo do sistema... Até logo"}')



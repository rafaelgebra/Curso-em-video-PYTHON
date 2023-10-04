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


def leia_Float(msg):
    while True:
        try:
            num = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número Real valido\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsúario interrompeu o programa\033[m')
            return 0
        else:
            return num

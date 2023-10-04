#Crie um código em python que teste se o site pudim está acessivel pelo computador usado.

from time import sleep
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br/')
except urllib.error.URLError:
    print('O site Pudim não está acessível no momento')
except KeyboardInterrupt:
    print('\033[31mUsúario interropeu o programa\033[m')
else:
    print('Consegui acessar o site Pudim com SUUUUUUU', end='', flush=True)
    for c in range(0, 20):
        sleep(0.4)
        print('U', end='')
    print('UCESO')
    print(site.read())

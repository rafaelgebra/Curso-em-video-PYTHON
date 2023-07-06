# ESTRUTURA DE REPETICAO COM TESTE LOGICO (WHILE) #
''' while not "apple":
    "passo"
"pega"
'''                # Estrutura#
'''    enquanto nao "apple"            while not "apple":
        se "chao"                       if "chao"
            "anda"                          "anda"
        se "buraco"                     if "buraco"
            "pula"                          "pula"
        se "moeda"                      if "moeda"
            "pega"                          "pega"
    "pega"                          "pega"
'''

'''from time import sleep
for c in range(1, 10):
    print(c, end=' ')
    sleep(0.2)
print('FIM')'''
from time import sleep
c = 1
while c < 10:
    print(c)
    sleep(0.2)

    c += 1
print('FIM')
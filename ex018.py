from math import radians,sin, cos, tan

ang =float(input('Digite um angulo '))
seno = sin(radians(ang))
print('O angulo de {} tem o SENO de {:.2f} '.format(ang, seno))
seno = cos(radians(ang))
print('O angulo de {} tem o COSSENO dee {:.2f}'. format(ang, seno))
tangente = tan(radians(ang))
print('O angulo de {} tem a TANGENTE de {:.2f}'.format(ang, tangente))

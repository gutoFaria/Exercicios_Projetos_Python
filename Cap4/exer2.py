import numpy as np

print('Valores de consseno, seno e tangente')
angulo = float(input('Digite o valor do angulo em graus:'))
rad = np.deg2rad(angulo)

print(angulo , ' em radianos é : ',rad) 
cosseno = np.cos(rad)
seno = np.sin(rad)
tangente = np.tan(rad)

print('cosseno de ',angulo,'é : ',cosseno)
print('seno de ',angulo,'é : ',seno)
print('tangente de ',angulo,'é : ',tangente) 
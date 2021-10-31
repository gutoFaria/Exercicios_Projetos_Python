import math

print('Valores de consseno, seno e tangente')
angulo = float(input('Digite o valor do angulo em graus:'))
rad = math.radians(angulo)

print(angulo , ' em radianos é : ',rad) 

cos = math.cos(rad)
sen = math.sin(rad)
tg = math.tan(rad)

print('cosseno de ',angulo,'é : ',cos)
print('seno de ',angulo,'é : ',sen)
print('tangente de ',angulo,'é : ',tg) 
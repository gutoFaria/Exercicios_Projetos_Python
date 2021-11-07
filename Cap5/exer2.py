t = int(input('Digite o valor total em segundos: '))
segundos = 0
minutos = 0
horas = 0

minutos = int(t/60)

if minutos >= 60:
    horas = int(minutos/60)
    print('horas: ', horas)
    minutos = minutos % 60
    print('minutos: ',minutos)
#     segundos = minutos % 60
#     print('segundos: ',segundos)


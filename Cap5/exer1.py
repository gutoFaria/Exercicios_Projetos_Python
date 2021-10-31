notas = float(input('Digite o valor em dinheiro: '))
r100 = 0
r50 = 0
r10 = 0
r1 = 0

if notas > 100:
    resto100 = int(notas/100)
    print('Notas de 100: ',resto100)
    r100 = notas % 100
    resto50 = int(r100 / 50)
    print('Notas de 50 : ',resto50)
    r50 = r100 % 50
    resto10 = int(r50 / 10)
    print('Notas de 10 :',resto10)
    r10 = r50 % 10
    resto1 = int(r10 / 1)
    print('Notas de 1 : ',resto1)
#elif  r100 > 50 and r100 < 100:
   
#elif r50 > 10 and r50 < 50:
   
#elif r10 > 0 and r10 < 10:
   











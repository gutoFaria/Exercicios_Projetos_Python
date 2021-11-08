n = int(input('Digite o tamanho da lista:'))
y=[]
i=0
while i < n:
    x=int(input('Digite o valor:'))
    y.append(x)
    i= i+1

print(y)
soma=0
for a in y:
    soma = soma +a

print('Soma = ',soma)
media = soma/len(y)
print('Média = ',media)
print('Maior valor = ',max(y))
print('Menor valor = ',min(y))
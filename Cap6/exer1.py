n = int(input('Digite um valor'))

print('Sequência fibonacci dos ', n ,' primeiros termos')
soma = 0
i = 0
print('1')
print('1')
x = n-2
a = 1
b =1

while i < x:
    soma = a + b
    print(soma)
    a = b
    b = soma
    i += 1
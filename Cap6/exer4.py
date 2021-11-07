escolha = 1
while escolha != 0:
    print('Digite [1] para somar dois números')
    print('Digite [2] para subtrair dois números')
    print('Digite [3] para multiplicar dois números')
    print('Digite [4] para dividir dois números')
    print('Digite [0] parar fechar o programa')
    escolha = int(input('Digite sua escolha:'))
    if(escolha == 1):
        a = int(input('Digite o valor:'))
        b = int(input('Digite o segundo valor:'))
        soma = a + b
        print(a, ' + ',b,' = ',soma)
    elif(escolha == 2):
        a = int(input('Digite o valor:'))
        b = int(input('Digite o segundo valor:'))
        soma = a - b
        print(a, ' - ',b,' = ',soma)
    elif(escolha == 3):
        a = int(input('Digite o valor:'))
        b = int(input('Digite o segundo valor:'))
        soma = a * b
        print(a, ' * ',b,' = ',soma)
    elif(escolha == 4):
        a = int(input('Digite o valor:'))
        b = int(input('Digite o segundo valor:'))
        soma = a / b
        print(a, ' / ',b,' = ',soma)
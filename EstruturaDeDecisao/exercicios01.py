#Faça um Programa que peça dois números e imprima o maior deles.

num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))

if num1 > num2:
    print(f'O numero {num1} é maior que o numero {num2}')
else:
    print(f'O numero {num2} é maior que o numero {num1}')
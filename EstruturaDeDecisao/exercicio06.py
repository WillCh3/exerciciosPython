# Faça um Programa que leia três números e mostre o maior deles.

num1 = int(input('Digite um numeros: '))
num2 = int(input('Digite um numeros: '))
num3 = int(input('Digite um numeros: '))

if num1 > num2 and num1 > num3:
    print(f'O numero {num1} é o maior numero')
elif num2 > num3 and num2 >num1:
    print(f'O numero {num2} é o maior numero')
else:
    print(f'O numero {num3} é o maior numero')
#Faça um Programa que leia três números e mostre-os em ordem decrescente.

num1 = int(input('Digite um numeros: '))
num2 = int(input('Digite um numeros: '))
num3 = int(input('Digite um numeros: '))

if num1 > num2 and num1 > num3:
    print(f'{num1}')
    if num2 > num3:
        print(f'{num2}')
        print(f'{num3}')
    else:
        print(f'{num3}')
        print(f'{num2}')

if num2 > num1 and num2 > num3:
    print(f'{num2}')
    if num1 > num3:
        print(f'{num1}')
        print(f'{num3}')
    else:
        print(f'{num3}')
        print(f'{num1}')

if num3 > num1 and num3 > num2:
    print(f'{num3}')
    if num1 > num2:
        print(f'{num1}')
        print(f'{num2}')
    else:
        print(f'{num2}')
        print(f'{num1}')
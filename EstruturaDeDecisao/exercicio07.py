#Faça um Programa que leia três números e mostre o maior e o menor deles

num1 = int(input('Digite um numeros: '))
num2 = int(input('Digite um numeros: '))
num3 = int(input('Digite um numeros: '))
min = 0
max = 0

if num1 > num2 and num1 > num3:
    max = num1
    if num2 < num3:
        min = num2
    else:
        min = num3
elif num2 > num1 and num2 > num3:
    max = num2
    if num3 < num1:
        min = num3
    else:
        min = num1
else:
    max = num3
    if num1 < num2:
        min = num1
    else:
        min = num2

print(f'O menor numero é: {min}\nE o maior numero é: {max}')
# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

import math

num1 = int(input('Digite um numero inteiro: '))
num2 = int(input('Digite um segundo numero inteiro: '))
num3 = float(input('Digite um numero flutuante: '))

print('\n')
print(f'O Dobro {num1} mais {num2 / 2} o resultado é {(num1 * 2) + (num2 / 2)}')
print(f'A soma do triplo de {num1} mais {num3} o resultado é {float((num1 * 3) + num3)}')
print(f'{num3} elevado ao Cubo é igual {pow(num3, 4)}')
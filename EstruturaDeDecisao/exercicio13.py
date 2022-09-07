# Faça um Programa que leia um número e exiba o dia correspondente da semana.
#  (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

semana = ['Domingo', 'Segunda', 'Terça-feira', 'Quarta-Ferira', 'Quinta-Feira', 'Sexta-Feira', 'Sábado']

dia = int(input('Digite um numero para o dia da senama: '))

print(f'O dia da semana é {semana[dia -1]}')
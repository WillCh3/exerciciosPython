# Faça um Programa que peça um número correspondente a um determinado ano
#  e em seguida informe se este ano é ou não bissexto

ano = int(input('Digite o Ano: '))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f'O ano de {ano} é Bissexto')
else:
    print(f'O ano de {ano}, não é bissexto')
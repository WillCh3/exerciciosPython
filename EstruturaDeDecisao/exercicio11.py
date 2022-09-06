'''
As Organizações Tabajara resolveram dar um aumento de salário 
aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, 
baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
'''

salario = float(input('Digite seu salário: '))
porc = 0

if salario >0 and salario <= 280.00:
    porc = (20/ 100) * salario
    print(f'Salario Antes do reajuste: {salario}')
    print(f'Percentual de aumento: 20%')
    print(f'Valor do aumento: R${porc}')
    print(f'Novo salário com aumento: R${salario + porc}')
elif salario > 280 and salario <= 700:
    porc = (15/ 100) * salario
    print(f'Salario Antes do reajuste: {salario}')
    print(f'Percentual de aumento: 15%')
    print(f'Valor do aumento: R${porc}')
    print(f'Novo salário com aumento: R${salario + porc}')
elif salario > 700 and salario <= 1500:
    porc = (10/ 100) * salario
    print(f'Salario Antes do reajuste: {salario}')
    print(f'Percentual de aumento: 10%')
    print(f'Valor do aumento: R${porc}')
    print(f'Novo salário com aumento: R${salario + porc}')
elif salario > 1500:
    porc = (5/ 100) * salario
    print(f'Salario Antes do reajuste: {salario}')
    print(f'Percentual de aumento: 15%')
    print(f'Valor do aumento: R${porc}')
    print(f'Novo salário com aumento: R${salario + porc}')
else:
    print(f'O Valor de {salario} é um salario invalido')

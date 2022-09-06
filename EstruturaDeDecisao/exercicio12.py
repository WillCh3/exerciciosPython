'''
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto
de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS 
corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). 
O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário
o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, 
dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00  
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00

'''

salario = float(input('Digite valor da hora: ')) * 220

if salario > 0 and salario <= 900:
    print(f'Salário Bruto : R$ {salario}')
    print(f'(-) IR : R$ 0.0')
    print(f'(-) FGTS  : R$ {(10/100) * salario}')
    print(f'Total de descontos  : R$ {(10/100) * salario}')
    print(f'Salario Liquido : R$ {salario - (10/100) * salario}')

elif salario > 900 and salario <= 1500:
    print(f'Salário Bruto : R$ {salario}')
    print(f'(-) IR : R$ {(5/100) * salario}')
    print(f'(-) FGTS  : R$ {(10/100) * salario}')
    print(f'Total de descontos  : R$ {((5/100) * salario + (10/100) * salario)}')
    print(f'Salario Liquido : R$ {salario - ((5/100) * salario + (10/100) * salario)}')

elif salario > 1500 and salario <= 2500:
    print(f'Salário Bruto : R$ {salario}')
    print(f'(-) IR : R$ {(10/100) * salario}')
    print(f'(-) FGTS  : R$ {(10/100) * salario}')
    print(f'Total de descontos  : R$ {((10/100) * salario + (10/100) * salario)}')
    print(f'Salario Liquido : R$ {salario - ((10/100) * salario + (10/100) * salario)}')

elif salario > 2500:
    print(f'Salário Bruto : R$ {salario}')
    print(f'(-) IR : R$ {(20/100) * salario}')
    print(f'(-) FGTS  : R$ {(10/100) * salario}')
    print(f'Total de descontos  : R$ {((10/100) * salario + (10/100) * salario)}')
    print(f'Salario Liquido : R$ {salario - ((10/100) * salario + (10/100) * salario)}')

else:
    print(f'Valor de salario invalido')
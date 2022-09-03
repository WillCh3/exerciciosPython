#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#  Calcule e mostre o total do seu salário no referido mês, sabendo-se que são 
# descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato,
#  faça um programa que nos dê:
#  salário bruto.
#  quanto pagou ao INSS.
#  quanto pagou ao sindicato.
#  o salário líquido.
#  calcule os descontos e o salário líquido, conforme a tabela abaixo:
#  + Salário Bruto : R$
#  - IR (11%) : R$
#  - INSS (8%) : R$
#  - Sindicato ( 5%) : R$
#  = Salário Liquido : R$

sal = float(input('Valor ganho por hora: '))

print('\n')
print(f'Salário bruto: R$:{sal * 220}')
print(f'Desconto IR: R$:{(sal * 220) * 11 / 100 }')
print(f'Desconto INSS: R$:{(sal * 220) * 8 / 100}')
print(f'Desconto sindicato: R$:{(sal * 220) * 5 / 100}')
print(f'Salário liquido: R$:{(sal * 2020) - ((sal * 2020) * 24 / 100)}')
print('\n')
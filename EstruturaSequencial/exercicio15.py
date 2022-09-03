sal = float(input('Valor ganho por hora: '))

print('\n')
print(f'Salário bruto: R$:{sal * 220}')
print(f'Desconto IR: R$:{(sal * 220) * 11 / 100 }')
print(f'Desconto INSS: R$:{(sal * 220) * 8 / 100}')
print(f'Desconto sindicato: R$:{(sal * 220) * 5 / 100}')
print(f'Salário liquido: R$:{(sal * 2020) - ((sal * 2020) * 24 / 100)}')
print('\n')
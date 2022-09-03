
altura = float(input('Digite sua altura: '))
sexo = input('Digite M para mulher e H para homen: ').upper()
print(sexo)

if sexo == 'H':
    print(f'Seu peso ideal é {(72.7 * altura) - 58:.2f}')
else:
    print(f'Seu peso ideal é {(62.1 * altura) - 44.7:.2f}')
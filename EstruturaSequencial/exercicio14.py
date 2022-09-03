
peso = float(input('Digite o peso do peixe: '))
excesso = 0

if peso > 50.0:
    print(f'\nPeso do peixe: {peso}')
    excesso = peso - 50.0
    print(f'Excesso: {excesso}')
    print(f'Multa: {excesso * 4.0}')
else:
    print(f'\nPeso do peixe: {peso}')
    excesso = 0.0
    print(f'Excesso: {excesso}')
    print(f'Multa: {excesso * 4.0}')
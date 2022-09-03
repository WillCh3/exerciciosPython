#Faça um programa para uma loja de tintas. O programa deverá pedir 
#  o tamanho em metros quadrados da área a ser pintada. Considere
#  que a cobertura da tinta é de 1 litro para cada 3 metros quadrados 
# e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
# Informe ao usuário a quantidades de latas de tinta
#  a serem compradas e o preço total.

print('\t lata de tintas ')
tamanho = float(input('Tamanho em metros quadrados: '))
litros = 18
latas = 0
preco = latas * 80

if tamanho % (litros * 3) == 0:
	latas = tamanho / (litros * 3)
else: 
	latas = int(tamanho / (litros * 3)) + 1


print (f'Vai precisar de {latas} latas')
print (f'Valor total: R$:{latas * 80}')
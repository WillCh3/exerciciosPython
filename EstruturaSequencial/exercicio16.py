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
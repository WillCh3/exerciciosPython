#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
# sabendo que a decisão é sempre pelo mais barato.

prod1 = float(input('Digite um valor: '))
prod2 = float(input('Digite um valor: '))
prod3 = float(input('Digite um valor: '))

if prod1 < prod2 and prod1 < prod3:
    print(f'O Produt 1 é o mais barato, com o valor de R$:{prod1}')
elif prod2 < prod3 and prod2 < prod1:
    print(f'O Produt 2 é o mais barato, com o valor de R$:{prod2}')
else:
    print(f'O Produt 3 é o mais barato, com o valor de R$:{prod3}')
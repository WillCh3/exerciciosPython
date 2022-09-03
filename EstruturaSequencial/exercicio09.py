#Faça um Programa que peça a temperatura em graus Fahrenheit, 
# transforme e mostre a temperatura em graus Celsius.
#   C = 5 * ((F-32) / 9).

fire = float(input('Digite os Graus Fahrenheit: '))

print(f'{fire}° Graus Fahrenheit convertidos para graus celcios fica em {(fire - 32) * 5/9:.2f}°')
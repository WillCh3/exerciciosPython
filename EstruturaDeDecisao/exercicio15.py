# Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar
#  se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo,
#  se o mesmo é: equilátero, isósceles ou escaleno.
#    Dicas:
#    Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#    Triângulo Equilátero: três lados iguais;
#    Triângulo Isósceles: quaisquer dois lados iguais;
#    Triângulo Escaleno: três lados diferentes;

t1 = float(input('Lado 1 do triangulo: '))
t2 = float(input('Lado 2 do triangulo: '))
t3 = float(input('Lado 3 do triangulo: '))

if t1 != t2 and t1 != t3 and t2 != t3:
    print(f'Triângulo  Escaleno medidas\nLado A: {t1}\nLado B: {t2}\nLado C: {t3}')

elif (t1 == t2 or t1 == t3 or t2 == t3) and (t1 != t2 or t1 != t3 or t2 != t3):
    print(f'Triângulo Isósceles medidas\nLado A: {t1}\nLado B: {t2}\nLado C: {t3}')

elif t1 == t2 and t2 == t3:
    print(f'Triângulo Equilátero medidas\nLado A: {t1}\nLado B: {t2}\nLado C: {t3}')
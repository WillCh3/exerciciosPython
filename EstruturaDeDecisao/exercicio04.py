#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input('Digite uma Letra: ').upper()
vogal ='AEIOU'

if letra in vogal:
    print(f'A letra {letra} é uma Vogal!')
else:
    print(f'A letra {letra} é uma Consoante!')

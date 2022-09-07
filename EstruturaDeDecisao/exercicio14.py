#Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina 
# ao longo de um semestre, e calcule a sua média. 
# A atribuição de conceitos obedece à tabela abaixo:
# Média de Aproveitamento  Conceito
# Entre 9.0 e 10.0        A
# Entre 7.5 e 9.0         B
# Entre 6.0 e 7.5         C
# Entre 4.0 e 6.0         D
# Entre 4.0 e zero        E

n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))

media = (n1 + n2) / 2

if media >= 9.0 and media <= 10:
    print(f' Média {media} Conveito A = Aprovado')
elif media >= 7.5 and media <9:
    print(f' Média {media} Conveito B = Aprovado')
elif media >= 6.0 and media <7.5:
    print(f' Média {media} Conveito C = Aprovado')
elif media >= 4.0 and media < 6:
    print(f' Média {media} Conveito D = Reprovado')
elif media >= 0 and media < 4.0:
    print(f' Média {media} Conveito E = Reprovado')
else:
    print(f'{media} Essa não é uma media válida')
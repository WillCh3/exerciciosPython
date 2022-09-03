# Faça um programa para a leitura de duas notas parciais de um aluno. 
# O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.

nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))

media = (nota1 + nota2) / 2

if media < 7:
    print(f'Nota {media}: Reprovado')
elif media == 10:
    print(f'Nota {media}: Aprovado com Distinção')
else:
    print(f'Nota {media}: Aprovado')
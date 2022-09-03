# Faça um Programa que verifique se uma letra digitada é "F" ou "M".
#  Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = input("Digite a letra M - Masculino e F feminino: ").upper()
print(sexo)
if sexo == 'M':
    print('Você é do sexo Masculino!')
else:
    print('Você é do sexo Feminino!')
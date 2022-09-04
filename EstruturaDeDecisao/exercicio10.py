#  Faça um Programa que pergunte em que turno você estuda.
#  Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
#  Imprima a mensagem "Bom Dia!", 
#  "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

turno = input('Digite M-matutino, V-Vespertino ou N-Noturno: ').upper()

if turno == 'M':
    print(f'Bom dia')
elif turno == 'V':
    print(f'Boa tarde')
elif turno == 'N':
    print('Boa noite')
else:
    print('Valor invalido!')
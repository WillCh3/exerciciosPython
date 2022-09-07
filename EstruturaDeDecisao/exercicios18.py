# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida

data = (input("Data, apenas numeros: "))
print(data[0:2])
print(data[2:4])
print(data[4:])
if int(data[0:2]) != 0  and int(data[0:2]) <= 31 :
    if int(data[2:4]) != 0  and int(data[2:4]) <= 12 :
        if int(data[4:]) != 0 :
            print("")
            print("Data Válida")
        else :
            print("")
            print("Data Inválida")
    else :
        print("")
        print("Data Inválida")
else:
    print("")
    print("Data Inválida")
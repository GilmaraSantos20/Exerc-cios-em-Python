
nota1 = float(input("Digite a primeira nota: "))
while nota1 < 0:
     print("Valor invalido! Tente novamente:")
     nota1 = float(input("Digite a primeira nota: "))
if nota1 > 0 and nota1 < 10:
    print(nota1)

nota2 = float(input("Digite a segunda nota: "))
while nota2 < 0:
     print("Valor invalido! Tente novamente:")
     nota2 = float(input("Digite a segunda nota: "))
if nota2 > 0 and nota2 < 10:
    print(nota2)


media = nota1 + nota2 / 2
print("A média é", media)
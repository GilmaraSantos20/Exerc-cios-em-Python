
a, b = str(input("Digite dois numeros  "))
print(a)
print(b)

if a != b:

    while a < b:
        print("Crescente!")
        a, b = input("Digite dois numeros  ")
    print(a)
    print(b)
    print("Decrescente")
else:
 print("Programa encerrado")
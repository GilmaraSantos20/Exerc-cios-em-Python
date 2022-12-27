A = float(input("Digite o valor de A: "))
B = float(input("Digite o valor de B: "))
C = float(input("Digite o valor de C: "))
raiz1 = float
raiz2 = float

delta = float(B * B - 4 * A * C)

if delta >= 0:
 raiz1 = - B + delta / (2 * A)
 raiz2 = - B - delta / (2 * A)
 print("{:.2f}".format(raiz1), "e", "{:.2f}".format(raiz2))

else:
    print("Nao possue raizes")
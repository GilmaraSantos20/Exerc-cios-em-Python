
x = int(input("Digite x:  "))
soma = 0

while x != 0:

    if x % 2 != 0:
        x = x + 1

    quant = x + 9

    for c in range(x, quant, 2):
      print(c)
      soma = soma + c
    print("SOMA = ",soma)
    x = int(input("Digite x:  "))

else:
    print("FIM")
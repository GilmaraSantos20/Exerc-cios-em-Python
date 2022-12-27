X = float(input("Primeira distância  "))
Y = float(input("Segunda distância  "))
Z = float(input("Terceira distância  "))

if X > Y and X > Z:
   print("A maior distâncuia foi a primeira", X)

elif Y > X and Y > Z:
   print("A maior distâncuia foi a segunda", Y)

else:
    print("A maior distâncuia foi a terceira", Z)
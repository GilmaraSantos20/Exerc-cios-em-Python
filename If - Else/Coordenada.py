x = float(input("Digite o valor de x"))
y = float(input("Digite o valor de y"))

if x > 0 and y > 0:
    print("Q1")
elif x < 0 and y > 0:
    print("Q2")

elif x < 0 and y < 0:
    print("Q3")

elif x > 0 and y < 0:
    print("Q4")

else: 
    print("Origem")
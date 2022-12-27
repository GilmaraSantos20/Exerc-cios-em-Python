x = float(input("Digite um numero:  "))
y =  float(input("Digite outro numero:  "))
resto1 = x % y
resto2 = y % x 

if resto1 or resto2 == 0: 
   print("São multiplos")
else:
    print("Não são multiplos")
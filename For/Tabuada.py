
x = int(input("Digite um numero:  "))
ordem1 = 0
ordem2 = x 
quant = x * 11 

for c in range(x, quant, x):
   ordem1 = ordem1 + 1
   print(ordem1, "X", ordem2, "=", c)
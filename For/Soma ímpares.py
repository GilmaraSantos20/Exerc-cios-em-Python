
'''Leia 2 valores inteiros X e Y (em qualquer ordem). A seguir, calcule e mostre a soma dos números 
impares entre eles. 
'''
x = int(input("Digite x:  "))
y = int(input("Digite y:  "))
soma = 0

for c in range(x, y):
    if c % 2 == 0:
        soma += 0
        
    else: 
        soma += c
print("SOMA DOS IMPARES =", soma)
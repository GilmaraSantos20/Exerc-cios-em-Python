
'''Digitar 6 números e somar apenas os pares'''

soma = 0 

for c in range (1, 7):
    num = int(input("Digite um numero "))
    if num % 2 == 0:
        soma += num 
        
    else: 
        soma += 0 
print(soma)
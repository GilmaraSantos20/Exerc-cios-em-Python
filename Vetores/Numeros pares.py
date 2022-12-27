
'''Faça um programa que leia N números inteiros e armazene-os em um vetor. Em seguida, mostre na
tela todos os números pares, e também a quantidade de números pares. 
'''

quant = int(input("Quantos numeros voce vai digitar? "))
quantPares = 0
pares = []

for c in range(0, quant):
    n = int(input("Digite um numero: "))
    if n % 2 == 0:
        pares.append(n)
        quantPares += 1

print("NUMEROS PARES: ")
print(pares)
print("QUANTIDADE DE PARES =", quantPares)
'''Faça um programa que leia N números reais e armazene-os em um vetor. Em seguida, mostrar na tela
o maior número do vetor (supor não haver empates). Mostrar também a posição do maior elemento,
considerando a primeira posição como 0 (zero). 
'''
quant = int(input("Quanto numeros voce vai digitar? "))
vet = []
maior = 1
posicao = 0

for c in range(0, quant):
    n = int(input("Digite um numero: "))
    vet.append(n)
    if n > maior:
        maior = n
        posicao += 1

print("MAIOR VALOR =", maior)
print("POSICAO DO MAIOR VALOR =", posicao)
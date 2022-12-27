
'''Faça um programa para ler dois vetores A e B, contendo N elementos cada. Em seguida, gere um
terceiro vetor C onde cada elemento de C é a soma dos elementos correspondentes de A e B. Imprima
o vetor C gerado'''


quant = int(input("Quantos valores vai ter cada vetor? "))
A = []
B = []
AB = []

for c in range(0, quant):
    a = int(input("Digite os valores do vetor A:"))
    A.append(a)
print(A)

for c in range(0, quant):
    b = int(input("Digite os valores do vetor B:"))
    B.append(b)
print(B)

AB = [A + B for A, B, in zip(A, B)]
print("VETOR RESULTANTE: ", AB)

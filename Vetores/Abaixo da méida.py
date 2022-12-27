
'''Fazer um programa para ler um número inteiro N e depois um vetor de N números reais. Em seguida, 
mostrar na tela a média aritmética de todos elementos com três casas decimais. Depois mostrar todos 
os elementos do vetor que estejam abaixo da média, com uma casa decimal cada.'''

quant = int(input("Quantos elementos vai ter o vetor? "))
soma = 0
vetAbaixo = []

for c in range(0, quant):
    n = float(input("Digite um numero: "))
    soma += n
    media = soma / quant
    if n < media:
        abaixo = n 
        vetAbaixo.append(abaixo)

print("MEDIA DO VETOR = ", media)
print("ELEMENTOS ABAIXO DA MEDIA: ")
print(vetAbaixo)
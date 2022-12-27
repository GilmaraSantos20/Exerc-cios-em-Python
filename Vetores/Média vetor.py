'''Faça um programa que leia N números reais e armazene-os em um vetor. Em seguida:
- Imprimir todos os elementos do vetor
- Mostrar na tela a soma e a média dos elementos do vetor '''


quant = int(input("Quantos numeros voce vai digitar? "))
valores = []
soma = 0

for c in range(0, quant):
    n = int(input("Digite um numero: "))
    valores.append(n)
    soma += n
    media = soma/quant
print(valores)
print(soma)
print(media)
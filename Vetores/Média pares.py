
'''Fazer um programa para ler um vetor de N números inteiros. Em seguida, mostrar na tela a média 
aritmética somente dos números pares lidos, com uma casa decimal. Se nenhum número par for 
digitado, mostrar a mensagem "NENHUM NUMERO PAR" '''

quant = int(input("Quantos elementos vai ter o vetor? "))
vetPares = []
soma = 0
repetido = 0

for c in range(0, quant):
    n = int(input("Digite um numero: "))
    if n % 2 == 0:
        vetPares.append(n)
        soma += n
        repetido += 1
    else:
        soma = 0

if soma > 0:
    media = soma / repetido
    print("MEDIA DOS PARES = ", media)
else: 
    print("NENHUM NUMERO PAR")
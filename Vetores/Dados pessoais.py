
'''Tem-se um conjunto de dados contendo a altura e o gênero (M, F) de N pessoas. Fazer um programa 
que calcule e escreva a maior e a menor altura do grupo, a média de altura das mulheres, e o número 
de homens. '''

quant = int(input("Quantas pessoas serao digitadas? "))
menorAlt = 9999
maiorAlt = 0
quantM = 0
quantF = 0
somaAltura = 0

for c in range(0, quant):

    print("Genero da", c + 1,"pessoa: (F/M) ")
    genero = str(input())

    print("Altura da ", c + 1," pessoa: ")
    altura = float(input())
    
    if genero == "M":
        quantM += 1

    else :
        somaAltura += altura
        quantF += 1
        mediaAltura = somaAltura/ quantF
   
    if altura < menorAlt:
        menorAlt = altura

    if altura > maiorAlt:
        maiorAlt = altura

print("Menor altura = ", menorAlt)
print("Menor altura = ", maiorAlt)
print("Media das alturas das mulheres =", mediaAltura)
print("Numero de homens", quantM)
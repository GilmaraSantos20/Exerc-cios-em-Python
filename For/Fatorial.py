
from socket import NI_NUMERICHOST
'''Fazer um programa para ler um número natural N (valor máximo: 15), e depois calcular e mostrar o 
fatorial de N. '''

n = int(input("Digite o valor de N: "))
fator = 1

if n <= 15:
    for c in range(4, 0, -1):
      fator = fator * c
    print(fator)
else:
    print("ERRO")
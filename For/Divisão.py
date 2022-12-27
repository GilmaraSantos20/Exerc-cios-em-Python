
'''Escreva um algoritmo que leia dois números e imprima o resultado da divisão do primeiro pelo 
segundo. Caso não for possível, mostre a mensagem “DIVISAO IMPOSSIVEL”'''

casos = int(input("Quantos casos voce vai digitar? "))

for c in range(0, casos):
   
   numerador = int(input("Entre com o numerador: "))
   denominador = int(input("Entre com o denominador: "))
   
   if denominador == 0:
    print("Divisão impossivel")
   else: 
    divisao = numerador / denominador
    print(divisao)

print("FIM")
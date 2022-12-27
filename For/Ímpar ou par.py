
'''Leia um valor inteiro N. Este valor será a quantidade de números inteiros que serão lidos em seguida. 
Para cada valor lido, mostre uma mensagem dizendo se este valor lido é PAR ou IMPAR, e também 
se é POSITIVO ou NEGATIVO. No caso do valor ser igual a zero (0), seu programa deverá imprimir 
apenas NULO. '''

quant = int(input("Quantos numeros voce vai digitar ?"))

for c in range(0, quant):
    n = float (input("Digite um numero: "))
    print(n)

    if n == 0:
        print("NULO")

    if n % 2 == 0 and n > 0:
        print("Par e positivo")

    if n % 2 == 0 and n < 0:
        print("Par e negativo")
    
    if n % 2 != 0 and n > 0:
        print("Impar e positivo")

    if n % 2 != 0 and n < 0:
        print("Impar e negativo")

print("FIM")
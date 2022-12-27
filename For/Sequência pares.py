
'''Leia um valor inteiro X. Em seguida mostre os ímpares de 1 até X, um valor por linha, inclusive o X, 
se for o caso. '''

x = int(input("Digite o valor de X: "))

if x % 2 != 0:
    x = x + 1

    for c in range(1, x, 2):
        print(c)

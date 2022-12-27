
'''Leia um valor inteiro N. Este valor será a quantidade de valores inteiros X que serão lidos em seguida. 
Mostre quantos destes valores X estão dentro do intervalo [10,20] e quantos estão fora do intervalo, 
conforme exemplo'''

n = int(input("Quantos numeros voce vai digitar?  "))
dentro = 0
fora = 0

for c in range(0, n):
   
    x = int(input("Digite um numero: "))
   
    if x >= 10 and x <= 20:
        dentro += 1
    else:
        fora += 1

print("Dentro do intervalo", dentro)
print("Fora do intervalo", fora)
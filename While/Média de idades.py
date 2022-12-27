
idade = float(input("Digite as idades: "))
soma = 0
quant = 0

while idade < 0:
 print("Imposssivel calcular")
 idade = float(input("Digite as idades: "))


while idade > 0:
    quant = quant + 1
    soma = soma + idade
    print(idade)
    idade = float(input("Digite as idades: "))

else:
    media = soma / quant
    print(media)

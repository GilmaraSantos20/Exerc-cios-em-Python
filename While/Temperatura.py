
tempC = float(input("Digite a temperatura em Fahrenheit"))
tempF = 9 * tempC / 5 + 32
resp = str

print("A temperatura em Fahrenheit é ",tempF)
resp = str(input("Deseja tentar novamente?"))

while resp != 'N':
    tempC = float(input("Digite a temperatura em Fahrenheit"))
    print("A temperatura em Fahrenheit é ",tempF)
    resp = str(input("Deseja tentar novamente?"))

print("Fim")
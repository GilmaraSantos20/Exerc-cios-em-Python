
codigo = int(input("Informe um codigo (1, 2, 3) ou 4 para parar: "))

while codigo != 4: 

 if codigo == 1:
    alcool = alcool + 1

 if codigo == 2:
    gasolina = gasolina + 1

 if codigo == 3:
    diesel = diesel + 1

 codigo = int(input("Informe um codigo (1, 2, 3) ou 4 para parar: "))

print("MUITO OBRIGADO")
print("Alcool", alcool)
print("Gasolina", gasolina)
print("Diesel", diesel)
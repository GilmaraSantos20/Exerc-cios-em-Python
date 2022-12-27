x = float(input("Digite a hora inicial:  "))
y = float(input("Digite a hora final:  "))
duracao = float

if x < y:
    duracao = y - x 
    print(duracao)

else:
    duracao = 24 - x + y
    print(duracao)

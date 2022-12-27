
'''Fazer um programa para ler nome, idade e altura de N pessoas, conforme exemplo. Depois, mostrar na
tela a altura média das pessoas, e mostrar também a porcentagem de pessoas com menos de 16 anos,
bem como os nomes dessas pessoas caso houver.'''

quant = int(input("Quantas pessoas serao digitadas? "))
alturasV = []
soma = 0
idadeMenor = 1
nomeMenor = []

for c in range(0, quant):
    print("Dados da ", (c + 1), " pessoa")
    nome = str(input("Nome: "))
    idade = int(input("Idade: "))
    altura = float(input("Altura: "))

    if idade < 16:
        idadeMenor =+ idadeMenor
        nomeMenor.append(nome)
    alturasV.append(altura)
    soma += altura

media = soma / quant
mediaIdadeMenor = idadeMenor / quant * 100
print("Altura média: ", media)
print("Pessoas com menos de 16 anos: ", mediaIdadeMenor, "%")
print(nomeMenor)

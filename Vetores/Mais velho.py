
'''Fazer um programa para ler um conjunto de nomes de pessoas e suas respectivas idades. Os nomes 
devem ser armazenados em um vetor, e as idades em um outro vetor. Depois, mostrar na tela o nome 
da pessoa mais velha. '''

quant = int(input("Quantas pessoas voce vai digitar?  "))
vetIdades = []
vetNomes = []
maiorIdade = 0
posicao = 0

for c in range(0, quant):
    print("Dados da ", (c + 1), "pessoa: ")
    
    nome = str(input("nome: "))
    vetNomes.append(nome)
    
    idade = int(input("idade: "))
    
    vetIdades.append(idade)
    if idade > maiorIdade:
        maiorIdade = idade
        posicao += 1

print("PESSOA MAIS VELHA: ", vetNomes[posicao - 1])
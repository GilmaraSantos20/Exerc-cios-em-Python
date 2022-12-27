from asyncore import read

quant = int(input("Quantos alunos serao digitados? "))
vetAprovados = []
vetNomes = []
for c in range(0, quant):
    print("Digite nome, primeira e segunda nota do ", c + 1, " aluno:")
    nome = input()
    N1 = int(input())
    N2 = int(input())
    soma = N1 + N2
    media = soma / 2
    if media >= 6:
        vetNomes.append(nome)
print("Alunos aprovados: ", vetNomes)
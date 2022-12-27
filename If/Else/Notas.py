nota1 = float(input ("Qual a primeira nota do aluno?"))
nota2 = float(input("Qual a segunda nota?"))
mediaNota = float((nota1 + nota2) / 2)

if mediaNota >= 60:
    print("A media é", mediaNota, ", aluno APROVADO")

else:
    print("A media é", mediaNota, ", aluno REPROVADO")
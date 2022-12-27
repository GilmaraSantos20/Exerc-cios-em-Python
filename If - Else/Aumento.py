salario = int(input("Digite o salario: "))
porcentagemAumento = 2.0
aumentoEmReais = 0
salarioFinal = 0

if salario <= 1000:
    porcentagemAumento = (20/100)
    aumentoEmReais = salario * porcentagemAumento
    salarioFinal = salario + aumentoEmReais

elif salario > 1000 and salario <= 3000:
    porcentagemAumento = (15/100)
    aumentoEmReais = salario * porcentagemAumento
    salarioFinal = salario + aumentoEmReais

elif salario > 3000 and salario <= 8000:
    porcentagemAumento = (10/100)
    aumentoEmReais = salario * porcentagemAumento
    salarioFinal = salario + aumentoEmReais

else: 
    porcentagemAumento = (5/100)
    aumentoEmReais = salario * porcentagemAumento
    salarioFinal = salario + aumentoEmReais 

print("Aumento em porcentagem: ", porcentagemAumento * 100, "%")
print("Aumento em reais: R$ ", aumentoEmReais)
print("O salario final é: R$ ", salarioFinal)
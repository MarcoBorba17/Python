salario = int(input("Insira seu Salário"))
tempo = int(input(" Tempo de Serviço"))
salario_atual = salario * 1.05
if tempo >= 5:
    print(f"Seu Salário é {salario_atual}")
else:
    print ("Não tem Bônus")

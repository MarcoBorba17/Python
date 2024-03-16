import random
print ("Bem Vindo ao Simulador de Dados para RPG")


dados = int(input("Quantos Dados serão usados?"))

#Chama a variável para fazer o cálculo abaixo
total = 0

#loop para realizar a rolagem a depender da quantidade de Dados que o usuário informar
for contagem in range(dados):

#Solicita a quantidade de lado que cada dado possuem
    lados = int(input("Digite o número de lados que cada um têm:"))

#Realiza a rolagem aleatória dos dados por vez
    resultado = random.randint(1,lados)

    print("Rolando...")
    print(f"Você rolou o seguinte número: {resultado}")

#Soma de resultado de cada rolagem aleatória de lado de dado
    total += resultado

print ("O total da soma dos dados é:", total)
                                 
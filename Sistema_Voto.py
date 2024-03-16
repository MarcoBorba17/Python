import os

# Esse programa conta a quantidade de votos

print("Bem Vindo ao Sistema de Contagem de Votos!!!")

candidato1 = 0
candidato2 = 0
candidato3 = 0
votos_validos = 0
numero_eleitores = int(input("Digite o número de eleitores: "))

while votos_validos < numero_eleitores:
    voto = int(input("Escolha entre os:\n 1 - candidato1\n 2 - candidato2\n 3 - candidato3\n"))
    os.system("cls")
    if voto == 1:
        candidato1 = candidato1 + 1
    elif voto == 2:
        candidato2 = candidato2 + 1
    elif voto == 3:
        candidato3 = candidato3 + 1
    votos_validos += 1
    os.system("cls")

print ("RESULTADO FINAL DESTA VOTAÇÃO:")

print("numero de votos do candidato 1:", candidato1)
print("numero de votos do candidato 2:", candidato2)
print("numero de votos do candidato 3:", candidato3)
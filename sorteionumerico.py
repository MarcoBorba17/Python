import random

numero_correto = []

numero_sorteado = random.randint(1, 10)

quantidade_chances = 3

while quantidade_chances > 0:

    print("quantidade_chances", quantidade_chances)


    palpite = int(input("Tente Acertar o numero de 1 a 10: "))

    if palpite == numero_sorteado:
        print("Parabéns! Você acertou")
        break
    elif palpite < numero_sorteado:
        print("O numero é maior:")
        quantidade_chances -= 1
    elif palpite > numero_sorteado: 
        print("O numero é menor:")
        quantidade_chances -= 1
    if quantidade_chances == 0:
        print("Que pena! Você perdeu! O numero era", numero_sorteado)
                                 
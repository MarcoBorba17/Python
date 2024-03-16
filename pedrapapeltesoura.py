import random

def jogo_pedra_papel_tesoura():
    print("Bem-vindo ao Jogo de Pedra, Papel e Tesoura!")

    while True:
        escolha = input("\nEscolha (1) Pedra, (2) Papel ou (3) Tesoura: ")
        computador = random.randint(1, 3)

        if escolha in ('1', '2', '3'):
            escolha = int(escolha)
            if escolha == computador:
                print(f"Empate! O computador também escolheu {escolha}.")
            elif (escolha == 1 and computador == 3) or (escolha == 2 and computador == 1) or (escolha == 3 and computador == 2):
                print(f"Você venceu! O computador escolheu {computador}.")
            else:
                print(f"Você perdeu! O computador escolheu {computador}.")
        else:
            print("Escolha inválida. Digite 1 para Pedra, 2 para Papel ou 3 para Tesoura.")

        jogar_novamente = input("\nDeseja jogar novamente? (s/n): ")
        if jogar_novamente.lower() != 's':
            break

if __name__ == "__main__":
    jogo_pedra_papel_tesoura()

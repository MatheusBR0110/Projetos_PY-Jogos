import random as rd

def jogar_adivinhacao():
    print("------------")
    print("Bem-Vindo ao jogo de adivinhação!")
    print("------------")

    n_secreto = rd.randrange(1, 1000)
    n_tentativas = 0
    rodada = 1
    pontos = 1000

    print("Níveis de dificuldade")
    print("\n(1) Fácil (2) Médio (3) Difícil (4) Aleatório\n")

    nivel = int(input("Defina um nível: "))

    if(nivel == 1):
        n_tentativas = 12
    elif(nivel == 2):
        n_tentativas = 6
    elif(nivel == 3):
        n_tentativas = 3
    else:
        n_tentativas = rd.randrange(1, 1000)

    for rodada in range(1,n_tentativas + 1):
        print(f"Tentativa {rodada} de {n_tentativas}")
        entrada = int(input("Digite um número de 1 a 1000: "))
        acerto = entrada == n_secreto
        entrada_maior = entrada == n_secreto
        entrada_menor = entrada < n_secreto

        if(entrada > 1000 or entrada < 1):
            print("O valor digitado não é permitido")
            continue

        print(f"Você digitou o número: {entrada}")

        if(acerto):
            print(f"Você acertou o número secreto. Parabéns!!!")
            print(f"Parabéns (ou não)! Você fez {pontos} pontos")
            break
        else:
            if(entrada_maior):
                print("O número digitado foi maior do que o número secreto")
            if(entrada_menor):
                print("O número digitado foi menor do que o número secreto")

        pontos_perdidos = n_secreto - entrada  
        pontos = pontos - pontos_perdidos
        rodada = rodada + 1

    print("FIm do Jogo!")

if(__name__ == "_main_"):
    jogar_adivinhacao()
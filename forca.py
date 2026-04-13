import random as rd

def mensagem_inicial():
    print("-------------------------------")
    print("\nBem vindo ao jogo da forca!\n")
    print("-------------------------------")

def seleciona_palavra_rd():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()
    posicao = rd.randrange(0,len(palavras))
    
    palavra_secreta = palavras[posicao].lower()

    return palavra_secreta
#0,5 de nota
def letras_corretas(palavra_secreta):
    return ["_" for letra in palavra_secreta]

def entrada_dados():
    chute = input("Escreva uma letra: ")
    chute = chute.strip().lower()
    return chute

def chute_correto(palavra_secreta, chute, letras_acertadas):
    #index define a posição da letra
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = letra
        index += 1
            
def jogar_forca():
    mensagem_inicial()
    palavra_secreta = seleciona_palavra_rd()
    letras_acertadas = letras_corretas(palavra_secreta)

    perdeu = False
    acertou = False
    erros = 0

    #Enquanto não acertar a palavra secreta
    while not perdeu and not acertou:
        chute = entrada_dados()

        if chute in palavra_secreta:
            chute_correto(palavra_secreta, chute, letras_acertadas)
        else:
            erros += 1

        perdeu = erros == 6
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)

if(__name__ == "__main__"):
    jogar_forca()

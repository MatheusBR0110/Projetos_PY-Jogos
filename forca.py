def jogar_forca():
    print("--------------------------")
    print("Bem-Vindo ao jogo da Forca")
    print("--------------------------")

    arquivo = open("Jogos/palavras.txt", "r")
    palavras = []

    for linha in palavras:
        linha = linha.strip()
        palavras. append(linha)
    
    palavra_secreta = "processador".upper()
    letras_acertadas = []

    for letra in palavra_secreta:
        letras_acertadas.append()

    perdeu = False
    acertou = False
    erros = 0

    while(not perdeu and not acertou):
        chute = input("Digite uma letra: ")
        chute = chute.strip().upper()

        #index define a posição da letra
        index = 0
        if(chute in palavra_secreta):
            for letra in palavra_secreta:
                if(chute.upper() == letra.upper()):
                    letras_acertadas[index] = letra
                index = index + 1       
        else:
            erros += 1
        perdeu = erros == 6
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)
        
        



if(__name__ == "__main__"):
    jogar_forca()
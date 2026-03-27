def jogar_forca():
    print("--------------------------")
    print("Bem-Vindo ao jogo da Forca")
    print("--------------------------")

    lista = []

    palavra_secreta = "processador".upper()
    letras_acertadas = ["_","_","_","_","_","_","_","_","_","_","_"]
    perdeu = False
    acertou = False

    while(not perdeu and not acertou):
        chute = input("Digite uma letra: ")
        chute = chute.strip()

        #index define a posição da letra
        index = 0

        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                letras_acertadas[index] = letra
                print(letras_acertadas)
            index = index + 1
        



if(__name__ == "__main__"):
    jogar_forca()
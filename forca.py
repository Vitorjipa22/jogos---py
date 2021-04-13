import random

def jogar():
    print()
    print('\t'*15, end = '')
    print("*********************************")
    print('\t'*15, end = '')
    print("***Bem vindo ao jogo da Forca!***")
    print('\t'*15, end = '')
    print("*********************************")

    palavra_secreta = define_palavra()
    letras_acertadas = ["_" for letra in palavra_secreta]
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0


    while(not enforcou and not acertou):

        chute = pedir_chute()

        if(chute in palavra_secreta):
            chute_certo(chute,palavra_secreta,letras_acertadas)
        else:
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

        print('')

    if(acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)


def define_palavra():
    arquivo = open("Palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()
    palavra_secreta = palavras[random.randrange(0, 4)]
    return palavra_secreta

def pedir_chute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    return chute

def chute_certo(chute,palavra_secreta,letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1

def imprime_mensagem_perdedor(palavra_secreta):
    print('\t'*15+"Puxa, você foi enforcado!")
    print('\t'*15+"A palavra era {}".format(palavra_secreta))
    print('\t'*15+"    _______________         ")
    print('\t'*15+"   /               \       ")
    print('\t'*15+"  /                 \      ")
    print('\t'*15+"//                   \/\  ")
    print('\t'*15+"\|   XXXX     XXXX   | /   ")
    print('\t'*15+" |   XXXX     XXXX   |/     ")
    print('\t'*15+" |   XXX       XXX   |      ")
    print('\t'*15+" |                   |      ")
    print('\t'*15+" \__      XXX      __/     ")
    print('\t'*15+"   |\     XXX     /|       ")
    print('\t'*15+"   | |           | |        ")
    print('\t'*15+"   | I I I I I I I |        ")
    print('\t'*15+"   |  I I I I I I  |        ")
    print('\t'*15+"   \_             _/       ")
    print('\t'*15+"     \_         _/         ")
    print('\t'*15+"       \_______/           ")

def imprime_mensagem_vencedor():
    print('\t'*15+"Parabéns, você ganhou!")
    print('\t'*15+"       ___________      ")
    print('\t'*15+"      '._==_==_=_.'     ")
    print('\t'*15+"      .-\\:      /-.    ")
    print('\t'*15+"     | (|:.     |) |    ")
    print('\t'*15+"      '-|:.     |-'     ")
    print('\t'*15+"        \\::.    /      ")
    print('\t'*15+"         '::. .'        ")
    print('\t'*15+"           ) (          ")
    print('\t'*15+"         _.' '._        ")
    print('\t'*15+"        '-------'       ")

def desenha_forca(erros):
    print('\t'*15+"  _______     ")
    print('\t'*15+" |/      |    ")

    if(erros == 1):
        print('\t'*15+" |      (_)   ")
        print('\t'*15+" |            ")
        print('\t'*15+" |            ")
        print('\t'*15+" |            ")

    if(erros == 2):
        print('\t'*15+" |      (_)   ")
        print('\t'*15+" |      \     ")
        print('\t'*15+" |            ")
        print('\t'*15+" |            ")

    if(erros == 3):
        print('\t'*15+" |      (_)   ")
        print('\t'*15+" |      \|    ")
        print('\t'*15+" |            ")
        print('\t'*15+" |            ")

    if(erros == 4):
        print('\t'*15+" |      (_)   ")
        print('\t'*15+" |      \|/   ")
        print('\t'*15+" |            ")
        print('\t'*15+" |            ")

    if(erros == 5):
        print('\t'*15+" |      (_)   ")
        print('\t'*15+" |      \|/   ")
        print('\t'*15+" |       |    ")
        print('\t'*15+" |            ")

    if(erros == 6):
        print('\t'*15+" |      (_)   ")
        print('\t'*15+" |      \|/   ")
        print('\t'*15+" |       |    ")
        print('\t'*15+" |      /     ")

    if (erros == 7):
        print('\t'*15+" |      (_)   ")
        print('\t'*15+" |      \|/   ")
        print('\t'*15+" |       |    ")
        print('\t'*15+" |      / \   ")

    print('\t'*15+" |            ")
    print('\t'*15+"_|___         ")
    print()

if(__name__ == "__main__"):
    jogar()
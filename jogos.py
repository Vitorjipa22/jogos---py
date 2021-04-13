import adivinhação
import forca

def escolher_jogo():
    print("\n\t\t\t\t\t\t\t\t\t\t\t*********************************")
    print("\t\t\t\t\t\t\t\t\t\t\t******* Escolha um jogo! ********")
    print("\t\t\t\t\t\t\t\t\t\t\t*********************************")

    print("Digite (1) para o jogo da forca e (2) para jogo da adivinhação")
    op = int(input("Qual jogo: "))

    while op not in [1,2]:
        print("Opção invalida, digite um número entre 1 e 2")
        op = int(input("Qual jogo: "))

    if op == 1:
        forca.jogar()
    elif op == 2:
        adivinhação.jogar()

if (__name__ == "__main__"):
    escolher_jogo()
import random

def jogar():
    print("\n\t\t\t\t\t\t\t\t\t\t\t*********************************")
    print("\t\t\t\t\t\t\t\t\t\t\tBem vindo ao jogo de adivinhação!")
    print("\t\t\t\t\t\t\t\t\t\t\t*********************************")

    numero_secreto = random.randrange(1,101)
    numero_tentativas = 0
    pontos = 1000

    print("\nEscolha a dificuldade com '1' para facil '2' para medio e '3' para dificil")
    dif = int(input("Dificuldade: "))

    while (dif not in [1,2,3]):
         dif = int(input("Número invalido, digite um numero entre 1,2 e 3: "))

    if dif == 1:
        numero_tentativas = 20
    if dif == 2:
        numero_tentativas = 10
    if dif == 3:
        numero_tentativas = 5

    for rodada in range (1,numero_tentativas+1):
        print("\nDigite um número entre 1 e 100")
        chute = int(input("Digite um numero: "))
        print(f"\ntentativa {rodada} de {numero_tentativas}")
        print("Você digitou", chute)

        if (chute < 1 or chute > 100):
            print("Digite um número entre 1 e 100")
            continue

        acertou = chute == numero_secreto
        menor = chute < numero_secreto
        maior = chute > numero_secreto

        if(acertou):
            print("Você acertou")
            break
        else:
            pontos = pontos - abs(chute - numero_secreto)
            if(maior):
                print("O número que você digitou é maior que o numero esperado")
            if(menor):
                print("O número que você digitou é menor que o numero esperado")

    print("\nFim de jogo")
    if (not acertou):
        print("O numero era: ", numero_secreto)
    else:
        print("Seus pontos: ",pontos)

if (__name__ == '__main__'):
    jogar()

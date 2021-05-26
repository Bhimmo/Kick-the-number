import random

nova = True

def tela():
    print("|||||     Bem Vindo     |||||")
    print("|||||     Ao Jogo       |||||")
    print("|||||  Acerte o número  |||||")

def jogo():
    while True:
        try:
            global nova
            numP = random.randint(1,100)
            num = int(input("\nDigite um número de 1 a 100\nResposta: "))
            tent = 1
            while num != numP:
                if num > 100 or num < 0:
                    print("\tSó pode números entre 1 e 100")
                if num < numP:
                    print("\tAumente seu número")
                    tent += 1
                if num > numP:
                    print("\tDiminua seu número")
                    tent += 1
                num = int(input("\n \033[31m Tente outro número: \033[m"))

            print("\n\033[32mPARABÉNS\033[m\n")
            print("Você acertou o número com {} tentativas\n".format(tent))
            ver = input("Deseja jogar novamente?(s/n): ")
            if ver.lower() == "s":
                tela()
                continue
            else:
                nova = False
                break
        except ValueError:
            print("\nDigite um número inteiro")

def main():
    while nova:
        tela()
        jogo()
    print("\n\033[35mFoi um prazer jogar com você\033[m")

main()

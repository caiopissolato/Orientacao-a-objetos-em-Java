import random

def jogar():
    print("--------")
    print("Adivinhe")
    print("--------")

    print("Níveis de dificuldade\n(1) Fácil (2) Médio (3) Difícil")
    nivel = int(input("Escolha um nível de dificuldade: "))

    # numero_secreto = round(random.random(1,101))  round serve para arredondar o valor, pois random.random() gera um float
    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000
    #print(numero_secreto)

    if(nivel == 1):
        print("\nVocê escolheu o modo Fácil!\n")
        total_de_tentativas = 20
    elif(nivel == 2):
        print("\nVocê escolheu o modo Médio!\n")
        total_de_tentativas = 10
    else:
        print("\nVocê escolheu o modo Difícil!\n")
        total_de_tentativas = 5

    for n in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(n, total_de_tentativas))
        chute = input("Digite um numero entre 1 e 100: ")

        if ((int(chute) < 1) or (int(chute) > 100)):
            print("Você deve digitar um valor entre 1 e 100!")
            continue #pula uma iteração do laço no qual ele está dentro

        print("Voce digitou: ", chute)

        acertou = int(chute) == numero_secreto
        maior = int(chute) > numero_secreto
        menor = int(chute) < numero_secreto

        if acertou:
            print("Você adivinhou o numero secreto.")
            break #para e vai para o próximo bloca de execução
        else:
            if maior:
                print("Você errou, o numero secreto é menor que", int(chute))
            elif menor:
                print("Você errou, o numero secreto é maior que", int(chute))
            pontos_perdidos = abs(int(chute) - numero_secreto)
            pontos = pontos - pontos_perdidos

        if total_de_tentativas == n:
            pontos = 0
            print("\nO número secreto é {}".format(numero_secreto))

    print("Você fez {} pontos".format(pontos))
    print("Fim de jogo.")

    print(type(acertou))

if(__name__ == "__main__"): #para executar o arquivo adivinhe.py pelo terminal
    jogar()
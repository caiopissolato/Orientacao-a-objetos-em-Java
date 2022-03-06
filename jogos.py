import adivinhe
import forca

print("-----------------")
print("---VAMOS JOGAR---")
print("-----------------")

print("(1) Jogo da Adivinhação (2) Jogo da Forca")
opc = int(input("Escolha um jogo: "))

if(opc == 1):
    print("Você escolheu o jogo da Adivinhação!")
    adivinhe.jogar()
elif(opc == 2):
    print("Você escolheu o jogo da Forca!\n")
    forca.jogar()
else:
    print("Você escolheu uma opção inválida!\n")
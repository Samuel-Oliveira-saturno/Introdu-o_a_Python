import forca
import adivinhacao

def escolha_jogo():
    print("*********************************")
    print("*******Escolher o seu jogo!*******")
    print("*********************************")

    print("(1) Forca  (2) Adivinhacao ")

    jogo = int(input("Qual jogo?"))

    if(jogo == 1):
        print("Jogando forca")
        forca.jogar()
    elif(jogo ==2):
        print("Jogando adivinhacao")
        adivinhacao.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()
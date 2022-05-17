from dataclasses import replace
import os
import random
import string

def guess_word( palabras):
    pass


def hang_play():
    with open("./files/data.txt", "r", encoding="utf-8") as f:
        #obtiene palabra al azar del archivo que se leyo
        palabras = random.choice([palabra.strip().upper() for palabra in f])
        with open("./files/adivina.txt", "w", encoding="utf-8") as f:
            for guion in palabras:
                #print(' _ ', end="")
                f.write(' _ ')
    print("¡Adivina la palabra! \n")
    with open("./files/adivina.txt", "r", encoding="utf-8") as f:
        for guion in f:
                print(guion)
    print("\n \n", palabras)
    cadena = [i for i in palabras]
    adivina = []
    for letra in cadena:
        caracter = input("Ingresa un caracter: ").upper()
        if caracter == letra:
            with open("./files/adivina.txt", "a+", encoding="utf-8") as f:
                f.write(caracter)
                for juego in f:
                    adivina.append(juego)
            print(adivina)
        else:
            print("ERROR")
        
        print(caracter)
        print(letra)
        adivina.append(caracter)
    print(adivina)
    print(cadena)
    if cadena == adivina:
        print("LE ATINASTE")
    else:
        print("PERDISTE")

def run():
    os.system("clear")
    hang_play()



if __name__=='__main__':
    run()
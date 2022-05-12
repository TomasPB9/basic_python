from pickle import FALSE


def primo(numero):

    contador = 0
    for i in range (1,numero+1):
        if i == 1 or i == numero:
            continue
        elif numero % i == 0:
            contador += 1
    if contador == 0:
        return True
    else:
        return False


def run():
    numero = int(input ("ingresa un numero: "))
    if (primo(numero)):
        print("Es numero primo: " + str(numero))
    else:
        print("No es numero primo: " + str(numero))


if __name__ == "__main__":
    run()
def divisors(num):
#challenge = usa palabras clave try, except, raise para elevar un error 
#si el usuario ingresa un numero negativo en nuestro programa de divisores
    try:
        if num <= 0:
            raise ValueError("No se puede ingresa un numero negativo")
        else:
            divisors = [i for i in range(1,num+1) if num%i ==0]
            return divisors
    except ValueError as ve:
        print(ve)
        return False


def run():
#si el usuario ingresa una letra en nuestro programa de divisores
    try:
        num = int(input("Ingresa el nùmero que deseas: "))
        print(divisors(num))
        print("Termino mi programa")
    except ValueError:
        print("Debes ingresa un nùmero")

if __name__ == '__main__':
    run()

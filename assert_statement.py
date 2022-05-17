def divisors(num):
    divisors = [i for i in range(1,num+1) if num%i ==0]
    return divisors

def run():
        num = input("Ingresa el nùmero que deseas: ")
        #verifica si el string es un numero o un numero positivo, de lo contrario lanza error msg
        assert num.isnumeric() or num.isdigit(), "Debes introducir un numero, o un numero positivo"
        print(divisors(int(num)))
        print("Termino mi programa")

if __name__ == '__main__':
    run()
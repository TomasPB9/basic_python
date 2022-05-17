
# lectura del archivo
def read():
    numers = []
    with open("./files/numbers.txt", "r",encoding="utf-8") as f:
        for line in f:
            numers.append(int(line))
    print(numers)

#escritura con sobreescritura
def write():
    names = ["Tomas", "Miguel", "Cristian", "Rocío"]
    with open("./files/names.txt", "w", encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")

# escritura sin sobrescritura (añade al final del arichvo las nuevas lineas)
def append():
    names = ["Lost", "Roky"]
    with open("./files/names.txt", "a", encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")


def run():
    read()
    write()
    append()



if __name__=='__main__':
    run()
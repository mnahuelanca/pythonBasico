import random

def generar_pw():
    mayus = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    minus = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    sim = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']

    caracteres = mayus + minus + num + sim

    pw = []

    for i in range (16):
        caracter_random = random.choice(caracteres)  #elige un caracter random de la lista caracteres y lo guarda en una variable
        pw.append(caracter_random) #agrega el caracter elejido al azar en la lista PW

    pw = "".join(pw) #convierte la lista en un string
    return pw

def run():
    pw = generar_pw()
    print('Tu nueva contraseña es: ' + pw)


if __name__ == '__main__':
    run()
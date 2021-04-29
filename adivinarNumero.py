import random  

def run():
    numero_aleatorio = random.randint(1, 50)
    numero_elegido = int(input("Elige un numero del 1 al 50: "))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print("Busca un numero mas grande")
        else:
            print("Busca un numero mas pequeño")
        numero_elegido = int(input("Elige otro numero: "))
    print("GANASTE!")


if __name__ == "__main__":
    run()
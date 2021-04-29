def palindromo(palabra):
    palabra = palabra.replace(" ", "") #elimina los espacios del parametro
    palabra = palabra.lower() #pasa a minuscula
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False


def run():
    palabra = input("Escribe una palabra: ")
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print("Es palindromo")
    else:
        print("No es palindromo")
    continuar = input('Quiere continuar con otra palabra? si=1 / no=2: ')
    while continuar == '1':
        return run()
    else:
        print('Hasta luego!')


if __name__ == "__main__":
    run()

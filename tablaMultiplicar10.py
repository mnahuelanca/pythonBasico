
menu = """
Bienvenido, seleccione la tabla de multiplicar que necesita ✔
2
3
4
5
6
7
8
9
10
"""

opcion = input(menu)
if opcion =="2":
    for i2 in range(1, 11): 
        resultado2 = 2*i2
        print("2 x " + str(i2) + " es igual a: " + str(resultado2))
elif opcion =="3":
    for i3 in range(1, 11): 
        resultado3 = 3*i3
        print("3 x " + str(i3) + " es igual a: " + str(resultado3))
elif opcion =="4":
    for i4 in range(1, 11): 
        resultado4 = 4*i4
        print("4 x " + str(i4) + " es igual a: " + str(resultado4))
elif opcion =="5":
    for i5 in range(1, 11): 
        resultado5 = 5*i5
        print("5 x " + str(i5) + " es igual a: " + str(resultado5))
elif opcion =="6":
    for i6 in range(1, 11): 
        resultado6 = 6*i6
        print("6 x " + str(i6) + " es igual a: " + str(resultado6))
elif opcion =="7":
    for i7 in range(1, 11): 
        resultado7 = 7*i7
        print("7 x " + str(i7) + " es igual a: " + str(resultado7))
elif opcion =="8":
    for i8 in range(1, 11): 
        resultado8 = 8*i8
        print("8 x " + str(i8) + " es igual a: " + str(resultado8))
elif opcion =="9":
    for i9 in range(1, 11): 
        resultado9 = 9*i9
        print("9 x " + str(i9) + " es igual a: " + str(resultado9))
elif opcion =="10":
    for i10 in range(1, 11): 
        resultado10 = 10*i10
        print("10 x " + str(i10) + " es igual a: " + str(resultado10))
else:
    print("Elige una opcion correcta")
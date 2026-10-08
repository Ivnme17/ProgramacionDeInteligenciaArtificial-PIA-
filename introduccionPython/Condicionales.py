# numero = int(input("Escribe un numero"))

# Bloque if

# if(numero >= 0):
#     print("El numero es positivos")


# Bloque if-else

# if(numero < 0):
#     print("El numero es negativo")
# else:
#     print("El numero es positivos")


# # pass sirve para dejar la funcion o el bloque de programacion para un futuro
# edad = int(input("Escribe una edad"))

# if(edad<120):
#     pass
# else:
#     print("No me lo creo")


# Programa que mezcle dos colores if-elif-else
# Se puede hacer con if-else debido a que solo tenemos dos opciones, pero si se quisiera escalar(agregar más colores) nos vendria mejor usar elif
# print("Este es un programa que mezcla dos colores")
# print("r. Rojo y a. Azul")

# color1 = input("Elija un color (r o a): ")

# if(color1 == "r"):
#     print("a.Azul y v.Verde")
#     color2 = input("Elija un color (a o v): ")
#     if(color2 == "a"):
#         print("La mezcla del color rojo y azul es morado")
#     elif(color2 == "v"):
#         print("La mezcla de color rojo y verde es marron")
# elif(color1 == "a"):
#     print("r.Rojo y v.Verde")
#     color2 = input("Elija un color (r o v): ")
#     if(color2 == "r"):
#         print("La mezcla del color azul y rojo es morado")
#     elif(color2 == "v"):
#         print("La mezcla de color azul y verde es cian")
# else: print("No has elegido ninguno de los dos colores")


# Bloque if donde se deben cumplir dos condiciones
# edad = int(input("Introduce una edad:"))
# if(edad >= 0 and edad < 18):
#     print("Es menor de edad")

# # Si tuviera que cumpliser una o mas usariamos or

# edad = int(input("Introduce una edad:"))
# if(edad >= 0 or edad < 18):
#     print("Es menor de edad")

# MATCH

dia = int(input("Introduce un numero del 1 al 7:"))

# match dia:
#     case 1:
#         print("Lunes")
#     case 2:
#         print("Martes")
#     case 3:
#         print("Miercoles")
#     case 4:
#         print("Jueves")
#     case 5:
#         print("Viernes")
#     case 6:
#         print("Sabado")
#     case 7:
#         print("Domingo")
#     case _:
#         print("No hay más dias")

# Con valores combinados

# match dia:
#     case 1:
#         print("Lunes")
#     case 2:
#         print("Martes")
#     case 3:
#         print("Miercoles")
#     case 4:
#         print("Jueves")
#     case 5:
#         print("Viernes")
#     case 6 | 7:
#         print("Fin de semana")
#     case _:
#         print("No hay más dias")

mes = 4

match dia:
    case 1 | 2 | 3 | 4 | 5 if(mes == 4):
        print("Dias entre semana del mes de abril")

'''
Ejercicio 9. Cálculo de áreas
Escriba un programa que pregunte primero si se quiere calcular el área de un triángulo o la de un
círculo. Si se contesta que se quiere calcular el área de un triángulo (escribiendo T o t), el programa
tiene que pedir entonces la base y la altura y escribir el área. Si se contesta que se quiere calcular el
área de un círculo (escribiendo C o c), el programa tiene que pedir entonces el radio y escribir el
área.
Se recuerda que el área de un triángulo es base por altura dividido por 2 y que el área de un círculo
es pi por el radio al cuadrado.
Nota: utilice como valor de pi el valor 3.141592.
'''
PI = 3.141592

opcion = input("¿Quieres calcular el área de un triángulo (T) o de un círculo (C)? ")

if opcion == "T" or opcion == "t":
    base = float(input("Escriba la base del triángulo: "))
    altura = float(input("Escriba la altura del triángulo: "))
    area = base * altura / 2
    print(f"Un triángulo de base {base} y altura {altura} tiene un área de {area}")
elif opcion == "C" or opcion == "c":
    radio = float(input("Escriba el radio del círculo: "))
    area = PI * radio ** 2
    print(f"Un círculo de radio {radio} tiene un área de {area}")
else:
    print("Opción no válida. Escribe T o C.")
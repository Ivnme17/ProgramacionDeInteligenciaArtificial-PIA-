'''
Ejercicio 8. Ecuación de segundo grado
Escriba un programa que pida los coeficientes de una ecuación de segundo grado (a x2 + b x + c =
0) y escriba la solución.
Se recuerda que una ecuación de segundo grado puede no tener solución, tener una solución única,
tener dos soluciones o que todos los números sean solución. Cuando hay dos soluciones, la fórmula
es x = (-b ± √(b2 - 4ac)) / (2a).
Estos son algunos ejemplos de posibles respuestas (el orden de los ejemplos no tiene por qué
corresponder con el orden de las condiciones).
'''
import math
# Importo la libreria math para poder usar el metodo de raiz cuadrada sqrt()
a = float(input("Escriba el valor del coeficiente a: "))
b = float(input("Escriba el valor del coeficiente b: "))
c = float(input("Escriba el valor del coeficiente c: "))

if a == 0:
    if b == 0:
        if c == 0:
            print("La ecuación tiene infinitas soluciones: todos los números son solución.")
        else:
            print("La ecuación no tiene solución.")
    else:
        x = -c / b
        print(f"La ecuación tiene una solución única: {x}")
else:
    discriminante = b**2 - 4 * a * c
    if discriminante > 0:
        x1 = (-b + math.sqrt(discriminante)) / (2 * a)
        x2 = (-b - math.sqrt(discriminante)) / (2 * a)
        print(f"La ecuación tiene dos soluciones: {x1} y {x2}")
    elif discriminante == 0:
        x = -b / (2 * a)
        print(f"La ecuación tiene una solución única: {x}")
    else:
        print("La ecuación no tiene solución real.")
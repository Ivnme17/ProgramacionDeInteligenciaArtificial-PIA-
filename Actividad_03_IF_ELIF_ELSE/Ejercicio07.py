'''
Ejercicio 7. Ecuación de primer grado
Escriba un programa que pida los coeficientes de una ecuación de primer grado (a x + b = 0) y
escriba la solución.
Se recuerda que una ecuación de primer grado puede no tener solución, tener una solución única, o
que todos los números sean solución. La fórmula de la solución es x = -b / a.
Estos son algunos ejemplos de posibles respuestas (el orden de los ejemplos no tiene por qué
corresponder con el orden de las condiciones)
'''
a = float(input("Escriba el valor del coeficiente a: "))
b = float(input("Escriba el valor del coeficiente b: "))

if a != 0:
    x = -b / a
    print(f"La ecuacion tiene una solución unica: {x}")
elif b == 0:
    print("La ecuacion tiene infinitas soluciones: todos los numeros son solucion.")
else:
    print("La ecuacion no tiene solucion.")
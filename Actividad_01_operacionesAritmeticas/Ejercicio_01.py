'''
Ejercicio 1. Media de dos números
Escriba un programa que pida dos números y que escriba su media aritmética.
Se recuerda que la media aritmética de dos números es la suma de ambos números dividida
por 2.
'''
num1 = float(input("Introduce un numero:"))
num2 = float(input("Introduce otro numero:"))

media = float(num1 + num2 / 2)

print(f"La media de {num1} y {num2} es: {media}")
'''
Ejercicio 2. Comparador de números
Escriba un programa que pida dos números y que conteste cuál es el menor y cuál el mayor o que
escriba que son iguales.
'''
num1 = float(input("Introduce un número: "))
num2 = float(input("Introduce otro número: "))

if(num1 > num2 ):
    print(f"Menor: {num2} Mayor: {num1}")
elif(num1 < num2):
    print(f"Menor: {num1} Mayor: {num2}")
elif(num1 == num2):
    print("Los dos números son iguales")

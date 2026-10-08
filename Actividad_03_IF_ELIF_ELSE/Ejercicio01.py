'''
Ejercicio 1. Divisor de números
1.1. División exacta
Escriba un programa que pida dos números enteros y que calcule su división, escribiendo si la
división es exacta o no.
'''

num1 = int(input("Introduce un número entero: "))
num2 = int(input("Introduce otro número entero: "))

division = round(num1 / num2)

resto = num1 % num2

if(resto == 0):
    print("La división es exacta.", end=" ")
elif(resto != 0):
    print("La división no es exacta.", end=" ")
    
print(f"Cociente {division}",end=" ")
print(f"Resto: {resto}")

'''
1.2. División por cero
Mejore el programa anterior haciendo que tenga en cuenta que no se puede dividir por cero.
'''

if(num1 !=0 and num2 != 0):
    division = round(num1 / num2)
    resto = num1 % num2
else: print("No se puede dividir por cero")

if(resto == 0):
    print("La división es exacta.", end=" ")
elif(resto != 0):
    print("La división no es exacta.", end=" ")
    
print(f"Cociente {division}",end=" ")
print(f"Resto: {resto}")

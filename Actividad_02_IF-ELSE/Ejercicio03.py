'''
Ejercicio 3. Avisos finales
Escriba un programa que pida primero un número par y a continuación un número impar (positivos o
negativos). En caso de que uno o los dos valores no sean correctos, se mostrarán uno o dos avisos.
'''

num1 = int(input("Introduce un numero par: "))
num2 = int(input("Introduce un numero impar: "))

if(num1 % 2 !=0 ):
    print("El número escrito no es par")

if(num2 % 2 ==0):
        print("El número escrito no es impar")

print("Ejecute el programa para intentarlo nuevamente")
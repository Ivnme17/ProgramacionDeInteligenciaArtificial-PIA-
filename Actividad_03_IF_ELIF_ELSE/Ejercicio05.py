'''
Ejercicio 5. Comparador de tres números
Escriba un programa que pida tres números y que escriba si son los tres iguales, si hay dos iguales o
si son los tres distintos.
'''

num1 = int(input("Introduce un numero: "))
num2 = int(input("Introduce un numero: "))
num3 = int(input("Introduce un numero: "))

if(num1 == num2 and num2 == num3):
    print("Los tres numeros son iguales")
elif(num1 == num2 and num2 != num3 or num1 != num2 and num2 == num3 or num2 != num1 and num1 == num3):
    print("Solo hay dos numeros que son iguales")
elif(not(num1 == num2 and num2 == num3)):
    print("Ningun numero es igual")
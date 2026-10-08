'''
Ejercicio 1. Aviso final único
Escriba un programa que pida primero un número par y luego un número impar (positivos o
negativos). En caso de que uno o los dos valores no sea correcto, se mostrará un único aviso.
'''
num1 = int(input("Introduce un numero par: "))
num2 = int(input("Introduce un numero impar: "))

if(num1 % 2 ==0 and num2 % 2 !=0):
    print("Gracias por su colaboración!")
else: 
    print("Los números pasados por teclado no son correctos")

print("Ejecute el programa para intentarlo nuevamente")
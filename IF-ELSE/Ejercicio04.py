'''
Ejercicio 4. Avisos inmediatos
Escriba un programa que pida primero un número par y a continuación un número impar (positivos o
negativos). En cada petición, si el valor no es correcto se mostrará un aviso.
'''
num1 = int(input("Introduce un numero par: "))
if(num1 % 2 !=0 ):
    print(f"El número {num1}  no es par")

num2 = int(input("Introduce un numero impar: "))

if(num2 % 2 ==0):
        print(f"El número {num2} no es impar")
        
print("Ejecute el programa para intentarlo nuevamente")
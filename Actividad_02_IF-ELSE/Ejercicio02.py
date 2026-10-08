'''
Ejercicio 2. Aviso inmediato
Escriba un programa que pida primero un número par (positivo o negativo) y si el valor no es
correcto, muestre un aviso. Si el valor es correcto, pedirá un número impar (positivo o negativo) y si
el valor no es correcto, mostrará un aviso.
'''
num1 = int(input("Introduce un numero par: "))

if(num1 % 2 ==0 ):
    num2 = int(input("Introduce un numero impar: "))
    if(num2 % 2 ==0):
        print("El número escrito no es impar")
else: 
    print("El número escrito no es par")

print("Ejecute el programa para intentarlo nuevamente")
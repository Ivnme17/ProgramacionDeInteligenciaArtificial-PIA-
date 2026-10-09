'''
Ejercicio 4. Comparador de múltiplos
4.1. ¿Es múltiplo?
Escriba un programa que pida dos números enteros y que escriba si el mayor es múltiplo del menor.
'''
num1 = int(input("Introduce un número: "))
num2 = int(input("Introduce otro número: "))

if(num1 > num2 ):
    multiplo = num1 % num2
    if(multiplo == 0):
        print(f"El numero {num1} es multiplo de {num2}")
    else: 
        print(f"El numero {num1} NO es multiplo de {num2}")

elif(num2 > num1):
    multiplo = num2 % num1  
    if(multiplo == 0):  
        print(f"El numero {num2} es multiplo de {num1}")
    else:
        print(f"El numero {num2} NO es multiplo de {num1}")

'''
4.2. Valores negativos o nulos
Mejore el programa anterior haciendo que el programa avise cuando se escriben valores negativos o
nulos.
'''

if(num1 >0 and num2 > 0):
    if(num1 >= num2 ):
        multiplo = num1 % num2
        if(multiplo == 0):
            print(f"El numero {num1} es multiplo de {num2}")
        else: 
            print(f"El numero {num1} NO es multiplo de {num2}")

    elif(num2 > num1):
        multiplo = num2 % num1  
        if(multiplo == 0):  
            print(f"El numero {num2} es multiplo de {num1}")
        else:
            print(f"El numero {num2} NO es multiplo de {num1}")
elif(num1 < 0 or num2 < 0):
    print("Este programa no permite valores negativos")
elif(num1 == 0 or num2 == 0):
    print("Este programa no permite valores nulos")

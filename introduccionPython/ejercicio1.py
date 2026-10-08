# 1. Pide dos numeros y una operacion (+,-,*,/) Muestra el resultado de la operacion 
# Controlar entrada de datos y capturar el error ValueError para que cuando se introduzca un float no chille el programa e informe al usuario.
#try
num1 = int(input("Introduce un numero por teclado:"))
#exception (ValueError):

num2 = int(input("Introduce el segundo numero por teclado:"))

operador = input("Introduce el operador o la operación:")

'''
if(operador == "+" or operador.lower() == "sumar"):
    print(num1 + num2)
elif(operador == "-"  or operador.lower() == "restar"):
    print(num1 - num2)
elif(operador == "/" or operador.lower() == "dividir"):
    print(num1 / num2)

elif(operador == "//" or operador.lower() == "division truncada"):
    print(num1 // num2)

elif(operador == "%" or operador.lower() == "resto"):
    print(num1 % num2)
elif(operador == "*" or operador.lower() == "multiplicar"):
    print(num1 * num2)    
else: print("Error no es ningun operador")
'''


match operador:
    case "+" | "suma": print(num1 + num2)
    case "-" | "restar" : print(num1 - num2)
    case "*" | "multiplicar" : print(num1 * num2)
    case "/" | "dividir"  if(num1 != 0 or num2 != 0): print(num1 / num2)
    case "//" | "division truncada" if(num1 != 0 or num2 != 0): print(num1 // num2)
    case "%" | "resto": print(num1 % num2)
    case _: print("Operador u operación no encontrada")
# Meter la division entre 0 y el caso por defecto ( _ )
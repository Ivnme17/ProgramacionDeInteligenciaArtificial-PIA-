'''
Ejercicio 6. Comprobador de años bisiestos
Escriba un programa que pida un año y que escriba si es bisiesto o no.
Se recuerda que los años bisiestos son múltiplos de 4, pero los múltiplos de 100 no lo son, aunque
los múltiplos de 400 sí.
'''

anio = int(input("Introduce un anio: "))

if(anio % 400 == 0):
    print(f"El anio {anio} es bisiesto porque es multiplo de 400")
elif(anio % 100 == 0):
    print(f"El anio {anio} NO es bisiesto porque es multiplo de 100 sin serlo de 400")
elif(anio % 4 == 0):
    print(f"El anio {anio} es bisiesto porque es multiplo de 4 sin serlo de 100")
else:
    print(f"El anio {anio} NO es bisiesto porque no es multiplo de 4")
    
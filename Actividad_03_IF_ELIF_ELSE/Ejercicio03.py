'''
Ejercicio 3. Comparador de años
3.1. Años pasados y años que faltan
Escriba un programa que pida el año actual y un año cualquiera y que escriba cuántos años han
pasado desde ese año o cuántos años faltan para llegar a ese año.
'''

anio_actual = int(input("Introduce el anio actual: "))

anio = int(input("Introduce un anio cualquiera: "))

if(anio_actual > anio):
    anios_pasados = anio_actual - anio
    print(f"Desde el anio {anio} han pasado {anios_pasados}")
elif(anio > anio_actual):
    anios_que_faltan = anio - anio_actual
    print(f"Faltan {anios_que_faltan} anios para que llegue el anio {anio}")
elif(anio_actual == anio):
    print("Son el mismo anio!!!!")
    
'''
3.2. Diferencia de un año
Mejore el programa anterior haciendo que, cuando la diferencia sea exactamente un año, escriba la
frase en singular.
'''
anio = int(input("Introduce un anio cualquiera: "))

if(anio_actual > anio):
    anios_pasados = anio_actual - anio
    print(f"Desde el anio {anio} han pasado {anios_pasados}")
elif(anio > anio_actual):
    anios_que_faltan = anio - anio_actual
    if(anios_que_faltan > 1):
        print(f"Faltan {anios_que_faltan} anios para que llegue el anio {anio}")
    else:
        print(f"Falta {anios_que_faltan} anio para que llegue el  {anio}")
elif(anio_actual == anio):
    print("Son el mismo anio!!!!")


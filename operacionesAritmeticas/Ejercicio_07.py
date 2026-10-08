'''
Ejercicio 7. Segundos a horas y minutos
Escriba un programa que pida una cantidad de segundos y que escriba cuántas horas,
minutos y segundos son.
'''

minutos = float(input("Introduce minutos"))

segundos = round(minutos * 60)

print(f"{minutos} minutos son {segundos} segundos")
'''
Ejercicio 6. Segundos a minutos
Escriba un programa que pida una cantidad de segundos y que escriba cuántos minutos
y segundos son.
'''

segundos = float(input("Introduce segundos"))

minutos = round(segundos / 60)

print(f"{segundos} segundos son {minutos} minutos")

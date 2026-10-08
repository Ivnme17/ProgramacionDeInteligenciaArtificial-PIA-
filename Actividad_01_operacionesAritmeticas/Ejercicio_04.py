'''
Ejercicio 4. Celsius a Fahrenheit
Escriba un programa que pida una temperatura en grados Celsius y que escriba esa
temperatura en grados Fahrenheit.
Se recuerda que la relación entre grados Celsius (C) y grados Fahrenheit (F) es la siguiente: 
F = 1,8 * C + 32
'''

temperatura_en_Celsius = float(input("Introduce una temperatura en grados Celsius:"))

celsius_a_fahrenheit = 1.8 * temperatura_en_Celsius + 32


print(f"La temperatura {temperatura_en_Celsius} ºC en Fahrenheit es de {celsius_a_fahrenheit} ºF")
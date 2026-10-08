'''
Ejercicio 5. Fahrenheit a Celsius
Escriba un programa que pida una temperatura en grados Fahrenheit y que escriba esa
temperatura en grados Celsius.
Se recuerda que la relación entre grados Celsius (C) y grados Fahrenheit (F) es la siguiente: C
= (F - 32) / 1,8
'''


temperatura_en_Fahrenheit = float(input("Introduce una temperatura en grados Fahrenheit:"))

fahrenheit_a_celsius = round((temperatura_en_Fahrenheit - 32)/1.8 , 1)


print(f"La temperatura {temperatura_en_Fahrenheit} ºF  en Celsius es de {fahrenheit_a_celsius} ºC")


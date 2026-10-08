'''
3.1. Pies y pulgadas
Escriba un programa que pida una distancia en pies y pulgadas y que escriba esa
distancia en centímetros.
Se recuerda que un pie son doce pulgadas y una pulgada son 2,54 cm.
'''

pies = float(input("Introduce una cantidad de pies:"))
pulgadas = float(input("Introduce una cantidad de pulgadas:"))

pies_a_pulgadas = pies * 12
pulgadas_totales = pies_a_pulgadas + pulgadas

centimetros = pulgadas_totales * 2.54

print(f"{pies} pies y {pulgadas} pulgadas son {centimetros} cm")

'''
3.2. Pulgadas
Escriba un programa que pida una distancia en pulgadas y que escriba esa distancia en
centímetros.
Se recuerda que una pulgada son 2,54 cm.
'''

pulgadas = float(input("Introduce una distancia de pulgadas:"))

centimetros = pulgadas * 2.54

print(f"{pulgadas} pulgadas son {centimetros} cm")

'''
3.3. Pies
Escriba un programa que pida una distancia en pies y que escriba esa distancia en
centímetros.
Se recuerda que un pie son doce pulgadas y una pulgada son 2,54 cm.
'''

pies = float(input("Introduce una cantidad de pies:"))

pies_a_pulgadas = pies * 12

pulgadas_totales = pies_a_pulgadas + 2.54

print(f"{pies} pies son {centimetros} cm")


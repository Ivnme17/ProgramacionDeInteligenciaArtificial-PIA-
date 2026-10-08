'''
Ejercicio 8. A gruesas y docenas
Escriba un programa que pida una cantidad y que escriba cuántas gruesas, docenas y
unidades son.
Se recuerda que una gruesa son doce docenas.
'''

cantidad = int(input("Introduce una cantidad(entera):"))

# Cuantas gruesas son Division de unidades entre 144 gruesas

gruesas = round(cantidad // 144)

resto_gruesas = gruesas % 144

#Cuantas docenas son  Division de gruesas entre 12 docenas
docenas = round(resto_gruesas // 12)
unidades_restantes = resto_gruesas % 12

print(f"La cantidad {cantidad} de unidades son; {gruesas} gruesas, {docenas} docenas y el resto de unidades son {unidades_restantes}")

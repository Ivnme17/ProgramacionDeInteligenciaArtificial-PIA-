'''
Ejercicio 10. Convertidor de cm a km, m y cm

10.1. Todas las unidades
Escriba un programa que pida una distancia en centímetros y que escriba esa distancia en
kilómetros, metros y centímetros (escribiendo todas las unidades).
'''
cm_total = int(input("Escriba una distancia en centímetros: "))

if cm_total <= 0:
    print("Escriba una distancia mayor que cero.")
else:
    km = cm_total // 100000
    resto = cm_total % 100000
    m = resto // 100
    cm = resto % 100
    print(f"{cm_total} centímetros son {km} km {m} m {cm} cm.")
    
'''
10.2. Sin unidades innecesarias
Mejore el programa anterior haciendo que no se escriban las unidades innecesarias (cuando el valor
es cero).
'''

if cm_total <= 0:
    print("Escriba una distancia mayor que cero.")
else:
    km = cm_total // 100000
    resto = cm_total % 100000
    m = resto // 100
    cm = resto % 100

    texto = f"{cm_total} centímetros son"
    if km > 0:
        texto += f" {km} km"
    if m > 0:
        texto += f" {m} m"
    if cm > 0:
        texto += f" {cm} cm"
    print(texto + ".")
    
    
'''
10.3. Con comas
Mejore el programa anterior haciendo que se escriban comas después de las unidades (excepto en la
última).
'''

if cm_total <= 0:
    print("Escriba una distancia mayor que cero.")
else:
    km = cm_total // 100000
    resto = cm_total % 100000
    m = resto // 100
    cm = resto % 100

    partes = []
    if km > 0:
        partes.append(f"{km} km")
    if m > 0:
        partes.append(f"{m} m")
    if cm > 0:
        partes.append(f"{cm} cm")

    print(f"{cm_total} centímetros son {', '.join(partes)}.")
    
'''
10.4. Con comas e «y»
Mejore el programa anterior haciendo que se escriba la conjunción «y» antes de la última unidad.
'''

if cm_total <= 0:
    print("Escriba una distancia mayor que cero.")
else:
    km = cm_total // 100000
    resto = cm_total % 100000
    m = resto // 100
    cm = resto % 100

    partes = []
    if km > 0:
        partes.append(f"{km} km")
    if m > 0:
        partes.append(f"{m} m")
    if cm > 0:
        partes.append(f"{cm} cm")

    if len(partes) == 1:
        texto = partes[0]
    else:
        texto = ", ".join(partes[:-1]) + " y " + partes[-1]

    print(f"{cm_total} centímetros son {texto}.")
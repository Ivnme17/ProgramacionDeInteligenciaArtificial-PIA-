'''
Ejercicio 2. Índice de masa corporal
Escriba un programa que pida el peso (en kilogramos) y la altura (en metros) de una
persona y que calcule su índice de masa corporal (IMC), con un decimal.
Se recuerda que el IMC se calcula con la fórmula: imc = peso / altura al cuadrado
'''

peso = float(input("Introduce tu peso(Kg):"))
altura = float(input("Introduce tu altura(cm):"))

icm = peso / altura ** 2

print(f"Tu indice de masa corporal (IMC) debido a tu peso ({peso}Kg) y tu altura ({altura}cm) es: {icm}")
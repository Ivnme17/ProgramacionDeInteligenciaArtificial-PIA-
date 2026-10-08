# Listas

primo = [1,2,3,7,11,13,17]
dias_laborables= ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
dias_no_laborables = ["Sabado", "Domingo"]
#Concatenar listas
dias_de_la_semana = dias_laborables+dias_no_laborables
peliculas = [["Senderos de Gloria",1957], ["Hannah y hermanas",1986]]
lista_vacia = []
nombre = "Pepe"
edad =  25
lista_personas = [nombre, edad]

print(primo[1])
#Agregar un valor a la ultima posicion
primo += [19]

print(primo[1:9])

del primo[4]

for i in primo:
    print(i, end=" ")

print("\nAl revés")
for i in range(len(primo)-1,-1,-1):
    print(primo[i], end=" ")

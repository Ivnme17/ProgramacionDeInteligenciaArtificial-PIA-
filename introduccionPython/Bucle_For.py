import random
# Bucle For para recorrer elementos que no son colecciones
contador = int(input("Introduce el numero de veces que se va a repetir el bucle"))
for i in range(contador):
    print(i, end= " ")
    

for j in range(contador):
    print("Hola", end= " ")
    
dado = random.randint(1,6)

saca_5 = False
contador_5 = 0
for i in range(contador):
    print(dado, end=" ")
    dado = random.randint(1,6)
    if(dado == 5):
        saca_5 = True
        contador_5 += 1
    
if(saca_5):
    print(f"Ha salido el lado 5 un total de {contador_5} veces")

print("fin")
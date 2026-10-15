'''
Reto 2. El reto de ahorro de las 52 semanas
El «reto de las 52 semanas» propone ahorrar 1 € la semana 1, 2 € la semana 2, 3 € la
semana 3… y así hasta 52 € la semana 52. Hay quien lo hace en modo inverso: empieza
ahorrando 52 € la semana 1, 51 € la semana 2… y termina con 1 € la semana 52.
Escribe un programa que pida una semana inicial, una semana final y si se quiere el
modo inverso (respuesta s/n). El programa debe mostrar:
• la lista de euros que se ahorran cada semana de ese periodo (ambas semanas incluidas),
en el orden en que se ahorran;
• el total ahorrado en el periodo.
Comprobaciones: las semanas están entre 1 y 52 y la final no es menor que la inicial; la
respuesta del modo es «s» o «n». Si algo no es válido, se muestra un aviso.
Requisitos: cada lista se obtiene con un solo range() (en el modo inverso, con paso
negativo); el total se calcula con sum() sobre el range.
Pregunta final: sin ejecutar el programa, ¿cuánto se ahorra en el año completo? ¿Y en
modo inverso? Comprueba después tu respuesta con el programa.
'''

semana_inicial = int(input("Introduce un número: "))
semana_final = int(input("Introduce otro número: "))
opcion = input("Quiere usar el modo inverso(S/N): ")

if(semana_inicial >= 1 and semana_inicial <=52 and semana_final > semana_inicial):
    if(opcion == "S"):
        lista_ahorro_inversa = list(range(semana_final,semana_inicial,-1))
        print(f"Se ahorra de la semana {semana_inicial} hasta la {semana_final} en modo inverso : ",lista_ahorro_inversa)
        print(f"Ahorro total: {sum(lista_ahorro_inversa)} €")
    else:
        lista_ahorro = list(range(semana_inicial,semana_final+1,1))
        print(f"Se ahorra de la semana {semana_inicial} hasta la {semana_final}: ",lista_ahorro)  
        print(f"Ahorro total: {sum(lista_ahorro)} € ")  
else:
    print("Vuelve a ejecutar el programa (La semana no es correcta y la semana final es menor que la inicial)")
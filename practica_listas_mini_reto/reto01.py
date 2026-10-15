'''
Reto 1. Mis turnos
Trabajas por turnos: empiezas un día concreto del mes y, a partir de ahí, te toca turno cada
cierto número de días.
Escribe un programa que pida el día en que empiezas, cada cuántos días tienes turno
y cuántos días tiene el mes. El programa debe mostrar:
• la lista de días del mes en que trabajas (el último día del mes también cuenta);
• cuántos turnos haces ese mes.
Después, pide un día del mes y dice si ese día trabajas o lo tienes libre. Si el día no existe
en el mes, lo indica.
Comprobaciones: el mes tiene entre 28 y 31 días; el día de inicio está entre 1 y el número
de días del mes; el número de días entre turnos es mayor que 0. Si algún dato no es válido,
se muestra un aviso y no se calcula nada.
Requisitos: la lista de turnos se obtiene con un solo range(); el número de turnos se
calcula con len(), sin contar a mano; para saber si un día es de trabajo se usa el operador in
sobre el range.
'''

dia = int(input("Introduce un día del mes: "))
margen_turnos = int(input("Cada cuantos dias tienes turnos? "))
mes_en_dias = int(input("Cuántos dias tiene el mes: "))

if(dia >=1 and dia <= 28 or dia >=1 and dia <=31):
    if(margen_turnos > 0):
        # Usar un range donde el inicio sea el dia elegido del mes, el final el dia total del mes y los pasos a traves de los turnos
        lista_turnos = list(range(dia,mes_en_dias+1,margen_turnos))
        print("Trabajas los dias:",lista_turnos)
        total_turnos = len(lista_turnos)
        print("Numero de turnos:",total_turnos)
        dia_a_consultar = int(input("Qué día quieres consultar si trabajas? "))
        if(dia_a_consultar in range(dia,mes_en_dias+1,margen_turnos)):
            print(f"El día {dia_a_consultar} trabaja")
        else:
            print(f"El día {dia_a_consultar} NO trabaja")
    else:
        print("El turno tiene que ser mayor a cero")
else:
    print("Error: Ejecute de nuevo el programa (Día no existente)")
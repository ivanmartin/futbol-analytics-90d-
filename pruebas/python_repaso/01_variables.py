#Introducir valor de pases totales y pases acertados
pases_totales = int(input("Introduzca el nº de pases intentados: "))
pases_acierto = int(input("Introduzca los pases acertados: "))

#Cálculo del porcentaje de acierto , pases acertados entre pases totales saca el factor 

porcentaje_acierto = pases_acierto / pases_totales * 100

print("El porcentaje de acierto es: " + str(round(porcentaje_acierto, 2)))

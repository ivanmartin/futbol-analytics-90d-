#Clasificar un tiro según su xG (>0,3 "ocasión clara", 0,1-0,3 "media", <0,1 "lejana").
x_G = float(input("Introduzca el xG esperado del tiro concreto: "))
if x_G < 0 or x_G > 1:
    print("El valor debe encontrarse entre 0 y 1")
else:
    if x_G > 0.3:
        print("Ocasión clara")

    elif x_G >=0.1:
        print("Ocasión media")

    else:
        print("Ocasión lejana")

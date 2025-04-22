a = 2
b = 2

if a == b:
    print("Son iguales")
elif a > b:
    print("A es mayor")
elif a < b:
    print("B es menor")

ingreso_mensual = 1000001

if ingreso_mensual > 100000:
    print("Ingreso alto")
elif ingreso_mensual > 50000 and ingreso_mensual <= 100000:
    print("Ingreso medio")
else:
    print("ingreso bajo")

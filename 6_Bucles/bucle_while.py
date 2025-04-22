#Ejemplo 1: Bucle while simple
#Este bucle while imprimirá los números del 0 al 4, ya que la condición contador < 5 se cumple.
contador = 0

while contador < 5:
    print(contador)
    contador += 1



#Ejemplo 2: Bucle while con continue y break
#Este bucle while imprimirá los números impares del 1 al 7 y luego saldrá del bucle cuando se alcance el número 7.
numero = 0

while numero < 10:
    numero += 1

    if numero % 2 == 0:
        # Si el número es par, continuamos con la siguiente iteración
        continue

    print(numero)

    if numero == 7:
        # Si el número es 7, salimos del bucle
        break


#Ejemplo 3: Bucle while con entrada del usuario
#En este ejemplo, el bucle while seguirá pidiendo al usuario que ingrese algo hasta que escriba "salir". 
# La función lower() se utiliza para hacer que la comparación sea insensible a mayúsculas y minúsculas.
respuesta = ""

while respuesta.lower() != "salir":
    respuesta = input("Ingrese 'salir' para finalizar: ")
    print(f"Usted ingresó: {respuesta}")


#Ejemplo 4: Bucle while con manejo de errores
#En este ejemplo, el bucle while continuará solicitando al usuario que ingrese un número entero 
# hasta que se proporcione una entrada válida. Se utiliza un bloque try-except para manejar errores 
# si el usuario ingresa algo que no se puede convertir a un número entero.
while True:
    try:
        numero = int(input("Ingrese un número entero: "))
        print(f"El doble del número ingresado es: {2 * numero}")
        break
    except ValueError:
        print("Error: Ingrese un número entero válido.")
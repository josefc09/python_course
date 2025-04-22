## Validando que solo ingresen un numero

while True:
    try:
        # Solicitar al usuario que ingrese un número entero
        input_usuario = input("Ingrese un número entero: ")

        # Intentar convertir la entrada a un entero
        numero_entero = int(input_usuario)

        # Si la conversión fue exitosa, salir del bucle
        break
    except ValueError:
        # Si ocurre un error al intentar convertir a entero,
        # informar al usuario y volver a solicitar la entrada
        print("Error: Por favor, ingrese un número entero válido.")

# Mostrar el número entero ingresado por el usuario
print(f"Ha ingresado el número entero: {numero_entero}")
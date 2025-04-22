def saludar():
    return "Hola a todos"

print(saludar())


def tabla(numero, operacion):
    operacion = operacion.lower()
    if operacion == "multiplicacion":
        for num in range(11):
            print(f"{numero} * {num} = {numero * num}")
    elif operacion == "suma":
        for num in range(11):
            print(f"{numero} + {num} = {numero + num}")
    elif operacion == "resta":
        for num in range(11):
            print(f"{numero} - {num} = {numero - num}")
    else:
        print(f"No encontrado")
    return

tabla(2, "multiplicacion")
tabla(2, "suma")
tabla(2, "resta")

def numero_maximo(numero1, numero2):
    maximo = max(numero1, numero2)
    return (numero1, numero2, maximo)

num1, num2, max = numero_maximo(5,4)

print(f"Entre el número {num1} y {num2} el máximo es {max}")
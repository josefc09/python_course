# Maneras de como definir una lista

lista1 = [1, "dos", 3.0, True]

#Usando la Función list():
lista2 = list([1, 2, 3, 4, 5])

#Lista Vacía:
lista_vacia = []

#Usando un for
numeros = [x for x in range(1, 6)]

#Usando el Método append():
lista = []
lista.append(1)
lista.append(2)
lista.append(3)

#Usando el Método extend():
lista = [1, 2, 3]
lista.extend([4, 5, 6])

#Usando la Función list() con Otra Secuencia (por ejemplo, una Tupla):
tupla = (1, 2, 3)
lista_desde_tupla = list(tupla)

#Usando el Método split() con una Cadena de Texto:
cadena = "a b c"
lista_desde_cadena = cadena.split()

#Usando Repetición:
lista_repetida = [0] * 5  # Crea una lista con cinco elementos 0


# Imprimiendo los datos
lista_datos = ["Jose", "Alberto", 28]

# Desempaquetado de datos
nombre, apellido, edad = lista_datos

# Impresión de datos de la lista
print(f"Lista de Datos: Nombre: {nombre} {apellido} y Edad: {edad}")

# Acceso a elementos de la lista con bucle for
print("Acceso a elementos con bucle for:")
for dato in lista_datos:
    print(dato)
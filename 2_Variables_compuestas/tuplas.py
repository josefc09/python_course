#Usando paréntesis:
tupla1 = ('cadena', 14, 3.14, True)

#Sin paréntesis (Empaquetado de Tupla):
tupla2 = 4, 5, 6

#Con un solo elemento (debe tener una coma al final):
tupla3 = (7,)

#Construcción de tuplas mediante la función tuple():
lista = [8, 9, 10]
tupla4 = tuple(lista)

#Usando la función zip() para combinar iterables:
nombres = ('Alice', 'Bob', 'Charlie')
edades = (25, 30, 22)
tupla5 = tuple(zip(nombres, edades))

#Desempaquetado de Tupla:
tupla6 = 11, 12, 13
a, b, c = tupla6  # Desempaquetado

#Creación de una tupla vacía:
tupla_vacia = ()

#Creación de una tupla con el constructor tuple():
tupla_construida = tuple()

#Usando comprensiones de tuplas:
tupla_comprension = tuple(x for x in range(5))


#Imprimir tuplas
mi_tupla = (1, 'dos', 3.0, True)

print("Tupla completa:", mi_tupla)

print("Primer elemento:", mi_tupla[0])
print("Segundo elemento:", mi_tupla[1])
print("Tercer elemento:", mi_tupla[2])
print("Cuarto elemento:", mi_tupla[3])

# Iterar sobre los elementos de la tupla e imprimirlos
print("Iterar e imprimir:")
for elemento in mi_tupla:
    print(elemento)
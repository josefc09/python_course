conjunto_vacio = set()

# Definición de un conjunto con elementos
conjunto1 = {1, 2, 3, 4, 5}

# Convertir una lista a un conjunto usando set()
lista = [3, 4, 5, 6, 7]
conjunto2 = set(lista)

# Acceder a elementos de un conjunto (los conjuntos no tienen índices)
# Por lo tanto, se utiliza un bucle para acceder a los elementos
print("Acceder a elementos:")
for elemento in conjunto1:
    print(elemento)

# Verificar si un elemento está en el conjunto
elemento_a_verificar = 3
print(f"¿El elemento {elemento_a_verificar} está en conjunto1?:", elemento_a_verificar in conjunto1)

# Operaciones con conjuntos (unión, intersección, diferencia)
conjunto3 = {4, 5, 6, 7, 8}
union = conjunto1.union(conjunto3)
interseccion = conjunto1.intersection(conjunto3)
diferencia = conjunto1.difference(conjunto3)

# Imprimir conjuntos y resultados de operaciones
print("Conjunto3:", conjunto3)
print("Unión de conjunto1 y conjunto3:", union)
print("Intersección de conjunto1 y conjunto3:", interseccion)
print("Diferencia entre conjunto1 y conjunto3:", diferencia)
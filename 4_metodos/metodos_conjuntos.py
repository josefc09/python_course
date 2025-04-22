conjunto = {1, 2, 3, 4, "hola"}

"""
add: Agregar un elemento al conjunto.
clear: Eliminar todos los elementos del conjunto.
copy: Crear una copia del conjunto.
difference: Obtener la diferencia entre dos conjuntos.
difference_update: Actualizar el conjunto restando elementos de otro conjunto.
discard: Eliminar un elemento específico del conjunto si está presente.
intersection: Obtener la intersección entre dos conjuntos.
intersection_update: Actualizar el conjunto manteniendo solo los elementos comunes.
isdisjoint: Verificar si dos conjuntos son disjuntos (no tienen elementos en común).
issubset: Verificar si un conjunto es subconjunto de otro.
issuperset: Verificar si un conjunto es superconjunto de otro.
pop: Eliminar y devolver un elemento arbitrario del conjunto.
remove: Eliminar un elemento específico del conjunto.
symmetric_difference: Obtener la diferencia simétrica entre dos conjuntos.
symmetric_difference_update: Actualizar el conjunto con su diferencia simétrica.
union: Obtener la unión de dos conjuntos.
update: Agregar elementos de otro conjunto al conjunto actual.
"""

conjunto = {1, 2, 3, 4, "hola"}

# add: Agregar un elemento al conjunto.
conjunto.add(5)
print("Conjunto después de agregar 5:", conjunto)

# copy: Crear una copia del conjunto.
conjunto_copia = conjunto.copy()
print("Copia del conjunto:", conjunto_copia)

# difference: Obtener la diferencia entre dos conjuntos.
otro_conjunto = {3, 4, 5, 6}
diferencia = conjunto.difference(otro_conjunto)
print("Diferencia entre conjuntos:", diferencia)

# difference_update: Actualizar el conjunto restando elementos de otro conjunto.
conjunto.difference_update(otro_conjunto)
print("Conjunto después de difference_update:", conjunto)

# discard: Eliminar un elemento específico del conjunto si está presente.
conjunto.discard(3)
print("Conjunto después de descartar 3:", conjunto)

# intersection: Obtener la intersección entre dos conjuntos.
conjunto_interseccion = conjunto.intersection(otro_conjunto)
print("Intersección entre conjuntos:", conjunto_interseccion)

# intersection_update: Actualizar el conjunto manteniendo solo los elementos comunes.
conjunto.intersection_update(otro_conjunto)
print("Conjunto después de intersection_update:", conjunto)

# isdisjoint: Verificar si dos conjuntos son disjuntos (no tienen elementos en común).
son_disjuntos = conjunto.isdisjoint(otro_conjunto)
print("¿Los conjuntos son disjuntos?:", son_disjuntos)

# issubset: Verificar si un conjunto es subconjunto de otro.
es_subconjunto = conjunto.issubset(otro_conjunto)
print("¿El conjunto es subconjunto?:", es_subconjunto)

# issuperset: Verificar si un conjunto es superconjunto de otro.
es_superconjunto = conjunto.issuperset(otro_conjunto)
print("¿El conjunto es superconjunto?:", es_superconjunto)

conjunto = {3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 7}
# pop: Eliminar y devolver un elemento arbitrario del conjunto.
elemento_eliminado = conjunto.pop()
print("Elemento eliminado con pop:", elemento_eliminado)

# remove: Eliminar un elemento específico del conjunto.
conjunto.remove(3)
print("Conjunto después de remover 3:", conjunto)

# symmetric_difference: Obtener la diferencia simétrica entre dos conjuntos.
diferencia_simetrica = conjunto.symmetric_difference(otro_conjunto)
print("Diferencia simétrica entre conjuntos:", diferencia_simetrica)

# symmetric_difference_update: Actualizar el conjunto con su diferencia simétrica.
conjunto.symmetric_difference_update(otro_conjunto)
print("Conjunto después de symmetric_difference_update:", conjunto)

# union: Obtener la unión de dos conjuntos.
union_conjuntos = conjunto.union(otro_conjunto)
print("Unión de conjuntos:", union_conjuntos)

# update: Agregar elementos de otro conjunto al conjunto actual.
conjunto.update(otro_conjunto)
print("Conjunto después de update:", conjunto)

# clear: Eliminar todos los elementos del conjunto.
conjunto.clear()
print("Conjunto después de clear:", conjunto)

diccionario1 = {
    'nombre': 'Alice',
    'edad': 25,
    'ciudad': 'Ejemplo'
}
print("Diccionario1:", diccionario1)

# Acceder a valores mediante llaves
nombre_dicc = diccionario1['nombre']
edad_dicc = diccionario1['edad']

# Creación de un diccionario desde listas de claves y valores usando zip()
claves = ['nombre', 'edad', 'ciudad']
valores = ['Bob', 30, 'Otro Ejemplo']
diccionario2 = dict(zip(claves, valores))
print("Diccionario2:", diccionario2)

# Creación de un diccionario mediante comprensión de diccionario
numeros = [1, 2, 3, 4, 5]
diccionario_cuadrados = {x: x**2 for x in numeros}
print("Diccionario de Cuadrados:", diccionario_cuadrados)

# Iterar sobre claves y valores de un diccionario
print("Iterar sobre claves y valores:")
for clave, valor in diccionario1.items():
    print(f"{clave}: {valor}")

# Creación de un diccionario con un solo elemento
diccionario_un_elemento = {'clave_unica': 'valor único'}
print("Diccionario con un solo elemento:", diccionario_un_elemento)

# Creación de un diccionario con la función dict() y una lista de tuplas clave-valor
lista_clave_valor = [('nombre', 'David'), ('edad', 28), ('ciudad', 'Ejemplo')]
diccionario_desde_lista = dict(lista_clave_valor)
print("Diccionario desde lista de tuplas:", diccionario_desde_lista)

# Creación de un diccionario con valores predeterminados usando fromkeys()
claves = ['nombre', 'edad', 'ciudad']
diccionario_con_valores_predeterminados = dict.fromkeys(claves, 'Valor Predeterminado')
print("Diccionario con valores predeterminados:", diccionario_con_valores_predeterminados)
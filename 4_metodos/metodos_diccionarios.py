

"""
 clear: Eliminar todos los elementos del diccionario
 copy: Crear una copia del diccionario
 fromkeys: Crear un nuevo diccionario con claves especificadas y un valor predeterminado
 get: Obtener el valor asociado con una clave (manejo seguro para evitar errores si la clave no existe)
 items: Obtener una vista de los pares clave-valor en el diccionario
 keys: Obtener una vista de las claves en el diccionario
 pop: Eliminar y obtener el valor asociado con una clave
 popitem: Eliminar y obtener un par clave-valor arbitrario del diccionario
 setdefault: Obtener el valor asociado con una clave; si la clave no existe, se agrega al diccionario con un valor predeterminado
 update: Actualizar el diccionario con pares clave-valor de otro diccionario
 values: Obtener una vista de los valores en el diccionario
 """


diccionario = {
    'nombre': "Jose",
    'apellido': "Fuentes",
    'edad': 28
}

print(dir(diccionario))


# Diccionario inicial
diccionario = {
    'nombre': "Jose",
    'apellido': "Fuentes",
    'edad': 28
}

# copy: Crear una copia del diccionario
diccionario_copia = diccionario.copy()

# fromkeys: Crear un nuevo diccionario con claves especificadas y un valor predeterminado
nuevo_diccionario = dict.fromkeys(['nombre', 'apellido', 'edad'], "Valor Predeterminado")

# get: Obtener el valor asociado con una clave (manejo seguro para evitar errores si la clave no existe)
valor_edad = diccionario.get('edad', "Clave no encontrada")

# items: Obtener una vista de los pares clave-valor en el diccionario
vista_items = diccionario.items()

# keys: Obtener una vista de las claves en el diccionario
vista_claves = diccionario.keys()

# pop: Eliminar y obtener el valor asociado con una clave
valor_apellido = diccionario.pop('apellido')

# popitem: Eliminar y obtener un par clave-valor arbitrario del diccionario
par_arbitrario = diccionario.popitem()

# setdefault: Obtener el valor asociado con una clave; si la clave no existe, se agrega al diccionario con un valor predeterminado
valor_nombre = diccionario.setdefault('nombre', "Valor Predeterminado")

# update: Actualizar el diccionario con pares clave-valor de otro diccionario
diccionario.update({'ubicacion': 'Ciudad X', 'ocupacion': 'Programador'})

# values: Obtener una vista de los valores en el diccionario
vista_valores = diccionario.values()

# clear: Eliminar todos los elementos del diccionario
diccionario.clear()

# Imprimir resultados
print("Diccionario original:", diccionario)
print("Copia del diccionario:", diccionario_copia)
print("Nuevo diccionario:", nuevo_diccionario)
print("Valor de 'edad':", valor_edad)
print("Vista de items:", vista_items)
print("Vista de claves:", vista_claves)
print("Valor eliminado ('apellido'):", valor_apellido)
print("Par arbitrario eliminado:", par_arbitrario)
print("Valor de 'nombre' después de setdefault:", valor_nombre)
print("Diccionario actualizado:", diccionario)
print("Vista de valores:", vista_valores)
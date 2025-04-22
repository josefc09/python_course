# los parámetros args sirven para poder agregar más variables a una función que no sea una lista

def suma(a,b):
    return a+b

print(suma(1,2))

# Si agregamos una variable c esto no funcionaría. Lo correcto sería

def suma(*numeros):
    return sum(numeros)

print(suma(1,2,3))
print(suma(1,2,3,4,5,6,7,8))

# Si queremos agregar más parámetros utilizamos *numeros al final
def suma(nombre, *numeros):
    return f"{nombre} la suma de tus número es {sum(numeros)}"

print(suma("Mario",1,2,3))

# Si agregamos una lista tambien funciona
# Esta es la forma óptima de sumar valores
def suma(numeros):
    print(f"No los suma...") 
    print(*numeros)
    print(f"Si los suma {sum([*numeros])}")
    
suma([1,2,3,4,5,6,7,8])


# Podemos cambiar el orden de los argumentos siempre y cuando agreguemos el nombre de la variable a cada entrada
def saludo_personalizado(nombre, apellido, adjetivo):
    return f"Hola {nombre} {apellido} eres un {adjetivo}"

print(saludo_personalizado("Pedro","Pérez","capo"))
print(saludo_personalizado(apellido="Pérez", nombre="Pedro",adjetivo="capo"))

# De igual manera podemos pre-definir los atributos 
def saludo_personalizado(nombre, apellido, adjetivo ="capo"):
    return f"Hola {nombre} {apellido} eres un {adjetivo}"

print(saludo_personalizado("Pedro","Pérez"))
print(saludo_personalizado(apellido="Pérez", nombre="Pedro",adjetivo="buenardo"))
# bucle for simple

animales = ["perro", "gato", "pollo","loro","tigre","leon","foca","jirafa","raton","cocodrilo"]
for animal in animales:
    print(animal)

numeros = [1,2,3,4,5,6,7,8,9,10,1,2,3,4,4,5,5]
for numero in numeros:
    print(f"{numero} * 7 = {numero * 7}")
    
    
# Recorriendo dos o más ciclos FOR con mismo número de elementos, si alguna lista tiene más elementos se itera el de menor cantidad de elementos
# Relacion [1:1]
for animal, numero in zip(animales, numeros):
    print(f"El {animal} tiene el número {numero}")
    
#Utilizando range
for num in range(3,5):
    print(f"numero: {num}")
    
for num in range(5):
    print(f"numero: {num}")

# Si queremos acceder a una lista podemos utilizar
for num in range(len(numeros)):
    print(f"numero: {num}")

# Sin embargo, lo CORRECTO es
for ind, num in enumerate(numeros):
    print(f"ind: {ind} y valor: {num}")


# For else
for numero in [1,2,3,4]:
    print(f"numero: {numero}")
else:
    print("Terminó")
  
    
#### ITERAR CONJUNTOS

# Ciclo FOR

animales = {"perro", "gato", "pollo","loro","tigre","leon","foca","jirafa","raton","cocodrilo"}
for animal in animales:
    print(animal)

numeros = {1,2,3,4,5,6,7,8,9,10,1,2,3,4,4,5,5}
for numero in numeros:
    print(f"{numero} * 7 = {numero * 7}")
    

# Recorriendo dos o más ciclos FOR con mismo número de elementos, si alguna lista tiene más elementos se itera el de menor cantidad de elementos
# Relacion [1:1]
for animal, numero in zip(animales, numeros):
    print(f"El {animal} tiene el número {numero}")
    
for num in range(3,5):
    print(f"numero: {num}")
    
for num in range(5):
    print(f"numero: {num}")

# Sin embargo, lo CORRECTO es
for ind, num in enumerate(numeros):
    print(f"ind: {ind} y valor: {num}")


for numero in {1,2,3,4}:
    print(f"numero: {numero}")
else:
    print("Terminó")


#### ITERAR tuplas

# Ciclo FOR

animales = ("perro", "gato", "pollo","loro","tigre","leon","foca","jirafa","raton","cocodrilo")
for animal in animales:
    print(animal)

numeros = (1,2,3,4,5,6,7,8,9,10,1,2,3,4,4,5,5)
for numero in numeros:
    print(f"{numero} * 7 = {numero * 7}")
    

# Recorriendo dos o más ciclos FOR con mismo número de elementos, si alguna lista tiene más elementos se itera el de menor cantidad de elementos
# Relacion [1:1]
for animal, numero in zip(animales, numeros):
    print(f"El {animal} tiene el número {numero}")
    
for num in range(3,5):
    print(f"numero: {num}")
    
for num in range(5):
    print(f"numero: {num}")

# Sin embargo, lo CORRECTO es
for ind, num in enumerate(numeros):
    print(f"ind: {ind} y valor: {num}")


for numero in (1,2,3,4):
    print(f"numero: {numero}")
else:
    print("Terminó")
    


#### Diccionarios

diccionario = {
    "nombre": "Jose",
    "apellido": "Fuentes",
    "edad": 20
}

for clave in diccionario:
    print(f"clave: {clave}")

for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f"{key} {value}")


frutas = ["manzana", "pera", "durazno", "platano", "ciruela", "naranja"]
for fruta in frutas:
    if fruta == 'pera': # si ya no tenemos pera no la muestra
        continue        
#        break # si queremos que termine al encontrar un elemento 
               # Nota: si hay else en el for lo omite
    print(f"Tenemos {fruta}")
    
    
    
### For en una sola linea
numeros = [1,2,3,4,5,6]
numeros = [x*2 for x in numeros]
print(numeros)
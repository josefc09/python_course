cadena1 = "Hola soy python"

"""
Funciones
    dir(variable) devuelve la lista de atributos válidos del objeto    
"""

print(dir(cadena1))

"""
Todos los métodos son funciones pero no todas las funciones son métodos
Los métodos son funciones específicas de objetos

Método
    variable.upper() Convierte a mayusculas
    variable.lower() Convierte en minisculas
    variable.capitalize() Convierte solo la primera en mayuscula
"""

cadena1 = "bienvenido"

print(cadena1.upper()) # bienvenido
print(cadena1.lower()) # BIENVENIDO
print(cadena1.capitalize()) # Bienvenido


"""
    variable.find("") Devuelve la posición iniciar donde encuentra el valor y -1 cuando no encuentra el valor
    variable.index("") Devuelve la posición iniciar donde encuentra el valor y ERROR cuando no encuentra el valor
"""
print("Hola a todos".find("a")) # 3
print("Hola a todos".index("a")) # 3


"""
    variable.isnumeric() Devuelve True o False si es numérico
    variable.isalpha() Devuelve True o False si es alfanumérico o solo letras (Regresa False si tiene espacios)
"""

print(cadena1.isnumeric()) # False
print(cadena1.isalpha()) # True


"""
    variable.count("") Devuelve las coincidencias dentro del texto
    len(variable) Devuelve el tamaño de una cadena
"""
print("Hola a todos".count("a")) # 2
print(len("Hola")) # 4


"""
    variable.startswith("") Verifica si una cadena empieza con ""
    variable.endswith("") Verifica si una cadena termina con ""
"""
print("Hola".startswith("H")) # True
print("Hola".endswith("a")) # True

"""
variable.replace(buscar,remplazar) Remplaza los valores que encuentra
variable.split() Separa todo por espacio
variable.split(",") Separa todo por coma
"""
print("Todo va bien".replace("bien","mal")) # Hola todo va mal
print("hola, hola".split()) # ['hola,', 'hola']
print("hola, hola".split(", ")) # ['hola', 'hola']


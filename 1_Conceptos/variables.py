# Definición de variables
nombre = "José"
apellido = " Fuentes"
edad = 28

# Concatenación con el operador '+'
nombre_completo = nombre + apellido

# Imprimir el nombre, apellido y edad concatenados
print("1. Concatenación con '+' (sin espacio):", nombre + apellido + " " + str(edad))

# Concatenación con f-string
mensaje_fstring = f"Hola {nombre_completo}, tu edad es {edad}"
print("2. Concatenación con f-string:", mensaje_fstring)

# Concatenación con el operador '+' y espacio adicional
mensaje_con_espacio = nombre + " " + apellido + " " + str(edad)
print("3. Concatenación con '+' (con espacio):", mensaje_con_espacio)


#Eliminar variables
cantidad = 12123
#del cantidad
print(cantidad) # -> Error


#operador de pertenencia (in y not in)
print("os" in nombre)  # True (José)
print("pepe" not in nombre) # True (José)



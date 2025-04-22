# Encoding UTF-8 sirver para que no nos de error los acentos (codificación universal)
archivo_sin_leer = open("9_Archivos\\texto.txt", encoding="UTF-8")

# Leemos el archivo completo
archivo_leido = archivo_sin_leer.read()
print(archivo_leido)

# Leemos el archivo por lineas 
archivo_por_lineas = archivo_sin_leer.readlines()
print(archivo_por_lineas)

# Leemos la primera linea del archivo   Si agregamos .readline(20) solo lee los primeros 20 caracteres
archivo_primera_linea = archivo_sin_leer.readline()
print(archivo_primera_linea)

#Cerramos el archivo
archivo_sin_leer.close()

####################################################################################################
####################################################################################################

# Abriendo archivos con with
with open("9_Archivos\\texto.txt", encoding="UTF-8") as archivo_sin_leer:
    archivo_primera_linea = archivo_sin_leer.readline()
    print(archivo_primera_linea)

    
#Escribir archivo txt
#w write a append 
with open("9_Archivos\\texto2.txt", 'w', encoding="UTF-8") as archivo:
    texto = """Escribiendo en el archivo\nRevisando si se escribió bien"""
    
    #sobre escribiendo el archivo
    archivo.write(texto)
    
    archivo.writelines(["\nAgregando más lineas","\nMuchas más"])
    

with open("9_Archivos\\texto2.txt", encoding="UTF-8") as archivo_sin_leer:
    archivo_primera_linea = archivo_sin_leer.read()
    print(archivo_primera_linea)
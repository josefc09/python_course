import re

texto = """Hola maestro, esta es la cadena 111, como estas mi capitan
esta es la segunda linea de texto (2. ) (probando abbb ababab)
Y esta es la tercera y definitiva capitanazo Hola
"""

#Busca la primera palabra dentro de la variable y retorna el inicio y final
# el parámetro flags=re.IGNORECASE sirve para no tomar en cuenta mayusculas y minusculas
resultado = re.search("Hola", texto)
inicio = resultado.start()
fin = resultado.end()
#resultado = re.findall("Hola", texto)
print(resultado)
print(f"El inicio es: {inicio} y el final es: {fin}")


"""
\d = Busca digitos numéricos del 0 - 9
\D = Busca TODO menos los digitos numéricos
\w = Busca caracteres alfanuméricos [a-z A-Z 0-9 _]
\W = Busca TODO menos caracteres alfanuméricos [a-z A-Z 0-9 _]
\s = Busca los espacios en blanco > espacios, tabs, saltos de linea
\S = Busca TODO menos los espacios en blanco > espacios, tabs, saltos de linea
\n = Busca saltos en linea
. = Busca todo menos saltos de linea
\ = Cancela caracteres especiales \. para buscar punto \_ para buscar _
^ = Busca el comienzo de una linea
$ = Busca el final de una linea
{n} = repite n cantidad de veces el valor de la izquierda
{n,m} = Busca como mínimo n y máximo m
| = Busca una cosa o la otra (si ambos cumples devuelve ambos)
* = Es un cuatificador que indica que el elemento precedente puede parecer cero o más veces
"""

# Buscando un numero, punto y espacio en blanco
resultados = re.findall(r"\d\.\s", texto)

# Buscando el principio de linea
resultados = re.findall(r"^Hola", texto)

# Buscando el principio de linea, pero si lo queremos multilinea
resultados = re.findall(r"^esta", texto, flags=re.M)

# Buscando el principio de linea
resultados = re.findall(r"Hola$", texto)
resultados = re.findall(r"capitan$", texto, flags=re.M)

# Buscar tres numeros juntos
resultados = re.findall(r"\d{3}", texto)
resultados = re.findall(r"1{3}", texto)

#Busca numeros con de uno a tres valores
resultados = re.findall(r"\d{1,3}", texto)

#Buscar una letra a seguida de tres b
resultados = re.findall(r"ab{3}", texto)

# Buscar tres a y tres b
resultados = re.findall(r"(ab){3}", "abababab ababab abc ab abab")
#regresa ['ab', 'ab'] porque solo abababab y ababab cumplen

resultados = re.findall(r"[ab]{3}", "abaaaabbabbbb")
#regresa ['aba', 'aaa', 'bba', 'bbb'] porque separa abaaaabbabbbb en grupos [aba aaa bba bbb] b

print(resultados)
# Si el modulo está en una carpeta
#      nombre_carpeta    .nom_modulo. función
import modulos_en_carpeta.m_en_carpeta
print(modulos_en_carpeta.m_en_carpeta.imprimir())

############################################################
############################################################

# Agregando un nombre a nuestro módulo
import modulos_en_carpeta.m_en_carpeta as saludar
print(saludar.imprimir())

############################################################
############################################################

# Agregando ruta a sys (Esto funciona por ejecución)

#Si el modulo está en otra ruta la podemos agregar al sistema con sys (modulo de python) ESTO ES TEMPORAL!
import sys

#esto es parecido a dir() y regresa todos los nombres de los modulos del dir
# Esto sirve para ver los modulo creados por python y que no exista uno repetido creado por nosotros ya que la prioridad siempre serán los nativos 
print(sys.builtin_module_names)

# Ver rutas de python
print(sys.path)

# Agregamos una ruta
sys.path.append("c:\\Users\\Jose\\Desktop\\Curso Python\\8_Modulos\\modulos_en_carpeta")
print(sys.path)

import m_saludar
print(m_saludar.saludar("Jose"))
#import m_saludo
#saludo = m_saludo.saludar("Jose")

# podemos asignar nombre a nuestro modulo
#import m_saludo as saludar
#saludo = saludar.saludar("Jose")
#print(saludo)

# Si queremos solo llamar a una función podemos utilziar

#from m_saludo import saludar
#from m_saludo import * # Cargar todo
from m_saludo import saludar, saludar_formal
saludo = saludar("Jose")
saludo_formal = saludar_formal("Jose")
print(saludo)
print(saludo_formal)


import m_saludo
# Si queremos ver propiedades del modulo
print(dir(m_saludo))

print(__name__)
print(m_saludo.__name__)
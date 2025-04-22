# Le llamamos importar paquete a importar varios modulos
import Paquete

# Si no tenemos el __init__.py esto da error
print(Paquete.__path__)

import Paquete.m_saludar
print(Paquete.m_saludar.saludar("Jose"))

########################################################################
########################################################################

from Paquete import m_saludar,m_despedir
print(m_saludar.saludar("Jose"))
print(m_despedir.despedir("Jose"))

########################################################################
########################################################################

#Nota: Si queremos acceder a un paquete dentro de un paquete (subpaquete)
import Paquete.Subpaquete.m_despedir 
from Paquete.Subpaquete import m_saludar as sub_paquete
print(sub_paquete.saludar("Mario"))
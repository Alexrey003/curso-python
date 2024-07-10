'EN CASO DE QUE NO FUNCIONE LA IMPORTACION DEL MODULO DEBEMOS ESPECIFICAR LA RUTA DONDE ENCONTRAREMOS NUESTRO MODULO'
import sys 
sys.path.append('C:/Users/Alexis/Desktop/ArchivosCurso/Curso python/EnrutModulos')

#Importando nuestro modulo desde una carpeta diferente
# import Directorio2.enrutamientoModulos2 as rut2

# # Directorio2.enrutamientoModulos2.saludo_mejorado()

# rut2.saludo_mejorado()

'Aqui importamos todas las funciones de nuestro modulo'
from Directorio2.enrutamientoModulos2 import *

saludo_mejorado()
sumas = suma(1,2 ,32,3,2,34,3,43,0)
print(sumas)
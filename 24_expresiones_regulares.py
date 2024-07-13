'''Expresiones regulares'''
import re #Importando el modulo regular expresion

texto = """Hola que tal tu dia, espero hayas tenido un buen dia, en caso de no:
No me importa
Porque aqui estoy yo para alegrarlo"""

#========================================================================================================

'Primera funcion de re (search()) sirve para buscar coincidencias'
"Esta funcion recibe dos parámetros, el primero lo que quieres biuscar y el segundo donde"
resultado_search = re.search("estoy", texto)
print (resultado_search, "\n")
#Solo encuentra una coincidencia

#========================================================================================================

'findall() encuentra todas las apariciones de un elemento que le hayamos pasado como paremetro'
#Los almacena en una lista
resultado_findall = re.findall(" ", texto)
print(resultado_findall, "\n")
'Aqui podemos agregar un tercer parámetro'
resultado_findall = re.findall("dia", texto, flags=re.IGNORECASE)
print(resultado_findall, "\n")

#========================================================================================================

'sub() sirve para reemplazar valores en una cadena de texto, recibiendo cuatro parámetros'
texto_2 = """Hola que tal estas Esta Esta el dia de hoy.
Esta es la cadena 1.
Esta es la linea 2.
Esta es la linea 3 y final.
"""
reemplazo = "Pizza"
resultado_sub = re.sub(r"^Esta", reemplazo, texto_2, flags=re.M)
print(resultado_sub, "\n")

#========================================================================================================
'''Primera expresion regular
\d --> Busca digitos numericos del 0 al 9 (1234567890)'''
texto_2 = """Hola que tal estas Esta Esta el dia de hoy.
Esta es la cadena 1.
Esta es la linea 2.
Esta es la linea 3 y final.
Numeros: 123456789101112
"""

#ESTO DIVIDIRA EN UNA LISTA QUE CONTENGA CADA DIGITO
resultado_d = re.findall(r"\d", texto_2)
print(resultado_d, "\n")
#========================================================================================================

'''Expresion regular:
\D --> Busca todo MENOS digitos del 0 al 9 (1234567890)'''
texto_2 = """Hola que tal estas Esta Esta el dia de hoy.
Esta es la cadena 1.
Esta es la linea 2.
Esta es la linea 3 y final.
Numeros: 123456789101112
"""
#Cuentan caracteres especiales y saltos de linea
resultado_D = re.findall(r"\D", texto_2)
print(resultado_D, "\n")

#========================================================================================================
'''Expresion regular:
\w --> Buscar caracteres alfanumericos [Aa - Zz, 0 - 9, _]'''
texto_2 = """Hola que tal estas Esta Esta el dia de hoy.
Esta es la cadena 1.
Esta es la linea 2.
Esta es la linea 3 y final.
Numeros: 123456789101112
"""
#No incluye caracteres especiales y saltos de linea, y espacios
resultado_w = re.findall(r"\w", texto_2)
print(resultado_w, "\n")
#========================================================================================================
'''Expresion regular:
\W --> Busca todo MENOS caracteres alfanumericos'''
texto_2 = """Hola que tal estas Esta Esta el dia de hoy.
Esta es la cadena 1.
Esta es la linea 2.
Esta es la linea 3 y final.
Numeros: 123456789101112
"""
resultado_W = re.findall(r"\W", texto_2)
print(resultado_W, "\n")
#========================================================================================================
'''Expresion regular:
\s --> Busca espacion en blanco, tabulación, saltos de linea'''
texto_2 = """Hola que tal estas Esta Esta el dia de hoy.
Esta es la cadena 1.
Esta es la linea 2.
Esta es la linea 3 y final.
Numeros: 123456789101112
"""
resultado_s = re.findall(r"\s", texto_2)
print(resultado_s, "\n")
#========================================================================================================
'''Expresion regular:
\S --> Busca todo MENOS espacion en blanco'''
texto_2 = """Hola que tal estas Esta Esta el dia de hoy.
Esta es la cadena 1.
Esta es la linea 2.
Esta es la linea 3 y final.
Numeros: 123456789101112
"""
resultado_S = re.findall(r"\S", texto_2)
print(resultado_S, "\n")
#========================================================================================================
'''Expresion regular:
. --> Busca todo MENOS saltos de linea'''
texto_2 = """Hola que tal estas Esta Esta el dia de hoy.
Esta es la cadena 1.
Esta es la linea 2.
Esta es la linea 3 y final.
Numeros: 123456789101112
"""
resultado_dot = re.findall(r".", texto_2)
print(resultado_dot, "\n")
#========================================================================================================
'''Expresion regular:
\n --> Busca saltos de linea'''
texto_2 = """Hola que tal estas Esta Esta el dia de hoy.
Esta es la cadena 1.
Esta es la linea 2.
Esta es la linea 3 y final.
Numeros: 123456789101112
"""
resultado_n = re.findall(r"\n", texto_2)
print(resultado_n, "\n")
#========================================================================================================
'''Expresion regular:
\caracter especial --> Busca caracteres especiales que indiquemos'''
texto_2 = """Hola que tal estas Esta Esta el dia de hoy.
Esta es la cadena 1.
Esta es la linea 2.
Esta es la linea 3 y final.
Numeros: 123456789101112
"""
resultado_especial = re.findall(r"\.", texto_2)
print(resultado_especial, "\n")
#========================================================================================================
'Podemos combinar las expresiones'
texto_2 = """Hola que tal estas el dia de hoy. Esta es la cadena 1.
Esta es la linea 2.
Esta es la linea 3. y final.
"""


resultado_combinado = re.findall(r'\d\.\s', texto_2)
print(resultado_combinado, "\n")

#========================================================================================================
'''Expresion regular:
^ --> Busca el comienzo de una linea'''
texto = """Hola que tal estas el dia de hoy. Esta es la cadena 1.
Esta es la linea 2.
Esta es la linea 3 y final.
"""
#ES MAS UTIL USARLO EN CONJUNTO
resultado_circun = re.findall(r'^', texto)

print(resultado_circun)

#========================================================================================================
'''flags = re.M --> Activa la busqueda en multilineas para expresiones regulares'''
texto_2 = """Hola que tal estas Esta Esta el dia de hoy.
Esta es la cadena 1.
Esta es la linea 2.
Esta es la linea 3 y final.
"""
reemplazo = "Pizza"
resultado_sub = re.sub(r"^Esta", reemplazo, texto_2, flags=re.M)
print(resultado_sub, "\n")

#========================================================================================================
''''Expresion regular:
$ --> Busca el final de una linea'''
texto = """Hola que tal estas el dia de hoy, esta es la cadena 1.
Esta es la linea 2.
Esta es la linea 3 y final.
"""

resultado_dolar = re.findall(r'.$', texto,flags=re.M)

print(resultado_dolar, "\n")
#========================================================================================================
'''Condicion:
{n} --> Busca lan-cantidad de veces el valor de la izquierda'''

texto = """Hola que tal estas el dia de hoy. Esta es la cadena 1.
Esta es la linea 223.
Esta es la linea 3 y final.
"""

resultado_n_cantidad = re.findall(r'\d{3}', texto)

print(resultado_n_cantidad, "\n")

'''Podemos agregar un máximo de m-cantidad de veces {n, m}'''

texto = """Hola que tal estas el dia de hoy. Esta es la cadena 1.
Esta es la linea 2 223.
Esta es la linea 3 y final.
12345678
"""
resultado_n_m_1 = re.findall(r'\d{1,4}', texto)

resultado_n_m_2 = re.findall(r'es{1,4}', texto, flags=re.IGNORECASE)

print(resultado_n_m_1, "\n")

print(resultado_n_m_2, "\n")

#NOTA: TAMBIEN SE PUEDE USAR EL OPERADORER OR | PARA EXPRESIONES REGULARES

#========================================================================================================
'ANALIZANDO UNA EXPRESION REGULAR COMPLEJA'

EMAIL = "alexrey003lol@gmail.com"

pattern = r"[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

resultado_match = re.match(pattern, EMAIL)

if resultado_match:
    print("Direccion de correo valida")
else:
    print("Direccion de correo invalida")

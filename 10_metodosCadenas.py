'Metodos de cadenas'

'''Estructura de una función
nombre_de_la_funcion(Objeto)'''

'Todo dentro de python es basicamente un objeto'
objeto1 = "Hola" #Objeto tipo str
objeto2 = 12 #Objeto tipo int
objeto3 = 12.4 #Objeto de tipo float
objeto4 = True #Objeto de tipo bool

# print(dir(objeto1))

'''Estrcutura métodos
objeto.nombre_del_metodo()'''

'Metodo upper'
cadena1 = "Hola me gustan los cocholates"

print("La cadena original es: {} \n".format(cadena1))

# resultado = Upper(cadena1) #Esto no es un método, por lo tanto dara error

'El método upper() nos va a devolver la cadena asociada a el en mayusculas'

resultado_metodo = cadena1.upper()

print("La cadena modificada con el metodo upper es: {}".format(resultado_metodo))
print("==================================================================")

#========================================================================================

'Metodo lower'
'''Este metodo lower() lo que hace es lo contrario al metodo upper(), nos devolvera toda
la cadena de texto en minusculas.'''

cadena2 = "HOLA MUNDO"
cadena3 = "HolA QuE tAl ValerIA"

print("""Las cadenas originales son:
{}
{}
""".format(cadena2, cadena3))

#Pasandole metodo lower()

resultado_lower1 = cadena2.lower()
resultado_lower2 = cadena3.lower()

print("""Las cadenas modificadas por el metodo lower son:
{}
{}""".format(resultado_lower1, resultado_lower2))
print("==================================================================")

# texto = input("Hola: ").lower() TAMBIEN SE PUEDE APLICAR LOS METODOS A LOS INPUTS DIRECTAMENTE
# print(texto)

#========================================================================================

'Metodo capitalize'
'Esto metodo capitalize() va a convertir la primera letra de nuestro str a mayusculas'
#NOTA: SOLO LA PRIMER LETRA DEL CADENA PASADA
#NOTA 2: ES COMO UNA COMBINACION DE LOS METODOS LOWER Y UPPER
cadena4 = "viva las vegas"
cadena5 = "VIVA LAS VEGAS"

print("""La cadena original es: 
{}
{}
""".format(cadena4, cadena5))

resultado_capitalize1 = cadena4.capitalize()
resultado_capitalize2 = cadena5.capitalize()

print("""La cadena modificada por el método capitalize es: 
{}
{}""".format(resultado_capitalize1, resultado_capitalize2))
print("==================================================================")

#========================================================================================

'Metodo find'
'''Este metodo find() va a encontrar la primera aparicion de un valor especificado (por nosotros),
si no se encuentra va a devolver -1.
El valor que devuelve es el indice de donde se encuentra el inicio del valor especificado'''

cadena6 = "Codigo en python 3.12.2"
cadena7 = "Deja a la pobre mosca"

print("""Las cadenas donde se buscaran los valores indicados seran:
{}
{}
""".format(cadena6, cadena7))

resultado_find1 = cadena6.find("th")
resultado_find2 = cadena7.find("on")

print("""El indice en donde se encuentra 'th' en la cadena 6 es el: 
°{} indice\n""".format(resultado_find1))

print("""El indice en donde se encuentra 'on' en la cadena 7 es el: 
°{} indice (NO SE ECUENTRA DICHO VALOR)""".format(resultado_find2))

#PYTHON ES CASE SENSITIVE AFECTAN MAYUSCULAS
print("==================================================================")

#========================================================================================

'Metodo index'
'''Este metodo index() es similar al método find(), la diferencia es que en caso de no encontrar una coincidencia'
en vez de devolver un -1, devolvera y tirara una excepcion'''

cadena8 = "Mi villano favorito"

print("La cadena donde buscaremos 'Mi' es: {}\n".format(cadena8))

resultado_index1 = cadena8.index("Mi")
# resultado_index1 = cadena8.index("MI") ESTO TIRARA UNA EXCEPCION

print("""El indice en donde se encuentra 'Mi' en la cadena 8 es el: 
°{} indice""".format(resultado_index1))
print("==================================================================")

#========================================================================================

'Metodo isnumeric'
'''Este metodo isnumeric() nos devolvera True si la cadena esta conformada por
puros numeros (1234567890)'''

cadena9 = "123456789101112131415"
cadena10 = "Abcd12345678910"

print("""Las cadenas que usaremos son: 
{}
{}
""".format(cadena9, cadena10))

resultado_isnumeric1 = cadena9.isnumeric()
resultado_isnumeric2 = cadena10.isnumeric()

print("¿La cadena 9 es numerica?: {}".format(resultado_isnumeric1))
print("¿La cadena 10 es numerica?: {}".format(resultado_isnumeric2))
print("==================================================================")

#========================================================================================
'Metodo isalpha'
'''Este metodo isalpha() nos devolvera True si la cadena esta conformada por caracteres
alfa-numericos (Aa - Zz)'''
#NOTA: LOS ESPACIOS SON CARACTERES INDIVIDUALES
cadena11 = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnÑñOoPpQqRrSsTtUuVvWwXxYyZz"
cadena12 = "ABCD''@."

print("""Las cadenas que usaremos son:
{}
{}
""".format(cadena11,cadena12))

resultado_isalpha1 = cadena11.isalpha()
resultado_isalpha2 = cadena12.isalpha()

print("¿La cadena 11 es alfanumerica?: {}".format(resultado_isalpha1))
print("¿La cadena 12 es alfanumerica?: {}".format(resultado_isalpha2))
print("==================================================================")

#========================================================================================
'Metodo count'
'Este metodo count() nos dira el numero de apariciones de un valor (dado ppor nosotros) en una cadena dada'

cadena13 = "Habia una vez una ave que podia volar, volaba y volaba sin cesár hasta que un dia se cayo de un puente y murio"

print("La cadena a utilizar sera: {}\n".format(cadena13))

resultado_count = cadena13.count("a")

print("Las veces que aparece el valor 'a' en la cadena 13 son: {}".format(resultado_count))
print("==================================================================")

#========================================================================================
'FUNCION LEN'
'Esta funcion len() nos devolvera la cantidad de caracteres que tiene una cadena de texto'
#NOTA: LOS ESPACIOS CUENTAN COMO CARACTERES
cadena14 = "Hola mundo de python"
cadena15 = "Adios mundo de python, gracias"

print("""Las cadenas a utilizar son:
{}
{}
""".format(cadena14, cadena15))

resultado_len1 = len(cadena14)
resultado_len2 = len(cadena15)

print("La cantidad de caracteres que tiene la cadena 14 son: {}".format(resultado_len1))
print("La cantidad de caracteres que tiene la cadena 15 son: {}".format(resultado_len2))
print("==================================================================")

#========================================================================================
'Metodo endswith'
'Este metodo endswith() verifica si en una cadena termina con un valor (dado por nosotros) en caso que se cumpla devolvera True'

cadena16 = "Me gusta el cocholate de vainilla"

resultado_endswith = cadena16.endswith("ta")

print(resultado_endswith)
print("==================================================================")

#========================================================================================
'Metodo startswith'
'Este metodo startswith() verifica si en una cadena inicia con un valor (dado por nosotros) en caso que se cumpla devolvera True'

cadena17 = "Parque Jurasico: El reino caido"

resultado_startswith = cadena17.startswith("Pa")

print(resultado_startswith)
print("==================================================================")

#========================================================================================

'Metodo replace'
'''Este metodo replace() reemplaza un valor por otro.
Este metodo tiene dos parametros:
1. El valor antiguo
2. El valor que rlo reemplazara'''

cadena18 = "Playas del Cozumel"

print(cadena18)

resultado_replace = cadena18.replace("Cozumel", "Carmen")

print(resultado_replace)
print("==================================================================")

#========================================================================================
'Metodo split'
'Este metodo va a separar por el parámetro dado la cadena de texto. (Nos devolvera una matriz/lista)'

cadena19 = "Curso python nivel intermedio"

resultado_split = cadena19.split(" ")

print(resultado_split)
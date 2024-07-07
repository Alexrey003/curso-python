'Dicciionarios'
'''Otra manera de crear diccionarios es mediante la sentencia dict'''

diccionario = dict(nombre = "Alexis", segundo_nombre = "Emanuel")
print(diccionario)

'Tambien con esta sentencia podemos crear diccionarios vacios'

'Las tuplas pueden ser llaves de un diccionario, pero listas y conjuntos (a menos que se use el frozenset) no'

diccionario = dict.fromkeys(["nombre", "apellido"], "VALOR 1")
print(diccionario)

diccionario = dict.fromkeys("ABCDEFGHIJK")
print(diccionario)
'PARA AGREGAR UN MISMO VALOR A CADA UNA DE ESTAS LLAVES'
diccionario = dict.fromkeys("ABCDEFGHIJK", "VALOR 1")
print(diccionario)

help(dict.values) #ESTO SIRVE PARA VER UNA DOCUMENTACION DEL OBJETO

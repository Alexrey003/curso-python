'Metodos diccionarios'

diccionario = {
    "Procesador" : 'Ryzen 9 9900X',
    "Ram" : '32GB',
    "Almacenamiento" : '5TB',
    "Fuente de poder" : 'Corsair 1500 watts',
    "Gabinete" : 'Yeyian Shadow 2200'
}
#=======================================================================================
'Metodo keys'
'Este metodo keys() nos devolvera las claves de nuestro diccionario'

print("El diccionario a utilizar es: ")
for key, value in diccionario.items():
    print("{}: {}".format(key, value))

resultado_keys = diccionario.keys()

print("\nLas llaves del diccionario son:\n{}".format(resultado_keys))
print("==================================================================")

#========================================================================================
'Metodo get'
'Este metodo get() nos va a devolver el valor de una llave'

print("\nEl diccionario a utilizar es: ")
for key, value in diccionario.items():
    print("{}: {}".format(key, value))

resultado_get = diccionario.get("Gabinete")
# resultado_get = diccionario.get("GaBINETE") SI LA LLAVE QUE PASAMOS COMO PARAMETRO NO SE ENCUENTRA DEVOLVERA NONE

print("\nEl valor de la llave 'Gabinete' es:\n{}".format(resultado_get))
print("==================================================================")

#========================================================================================
'Metodo clear'
'Este metodo clear() eliminara todos los elementos de nuestro diccionario'

print("\nEl diccionario a utilizar es: ")
for key, value in diccionario.items():
    print("{}: {}".format(key, value))

resultado_clear = diccionario.clear()

print("\nAl usar el metodo clear obtenemos un diccionario vacio:\n{}".format(diccionario))
print("==================================================================")

#========================================================================================
'Metodo pop'
'Este metodo pop() eliminara un elemento de la diccionari que nosotros le indicaremos'

diccionario = {
    "Procesador" : 'Ryzen 9 9900X',
    "Ram" : '32GB',
    "Almacenamiento" : '5TB',
    "Fuente de poder" : 'Corsair 1500 watts',
    "Gabinete" : 'Yeyian Shadow 2200'
}

print("\nEl diccionario a utilizar es: ")
for key, value in diccionario.items():
    print("{}: {}".format(key, value))

resultado_pop = diccionario.pop("Ram")

print("\nEl diccionario nuevo despues de eliminar la llave 'Ram' es:")
for key, value in diccionario.items():
    print("{}: {}".format(key, value))
# print(resultado_keys)
print("==================================================================")

#========================================================================================
'Metodo items'
'Este metodo items() sirve para iterar nuestro diccionario'
#NOTA: ITERAR ES RECORRER UN ELEMENTO
print("\nEl diccionario a utilizar es: ")
for key, value in diccionario.items():
    print("{}: {}".format(key, value))

resultado_items = diccionario.items()

print("\nEl diccionario iterado es:\n{}".format(resultado_items))

# print(dir(diccionario))
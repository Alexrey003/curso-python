'Metodos de listas'

'Manera tres de crear listas, es una manera muy poco utilizada'
# lista = list(["Cocholate", 21, 34.65, True])
#=================================================================================
'Metodo/Funcion len'
'Este metodo/funcion cuenta la cantidad de elementos de una lista'

lista = list(["Cocholate", 21, 34.65, True, "Mundo"])

print("""\nLa lista que usaremos es:
{}
""".format(lista))

resultado_len = lista.__len__()

print("La cantidad de elementos que contiene nuestra lista es de: {}".format(resultado_len))

resultado_len = len(lista)

print(resultado_len)
print("==================================================================")

#========================================================================================
'Metodo append'
'Este metodo append() agregara un nuevo elemento a la lista'

lista = list(["Cocholate", 21, 34.65, "Mundo"])

print("""\nLa lista que usaremos es:
{}
""".format(lista))

resultado_append = lista.append(50)
resultado_append = lista.append(False)
resultado_append = lista.append("Hola")

#NOTA: SE PASA LA LISTA PARA NO OBTENER UN NONE
print("La lista nueva que tenemos al agregr los nuevos valores es:\n{}".format(lista))
print("==================================================================")

#========================================================================================
'Metodo insert'
'Este metodo insert() agrega un nuevo elemento a la lista en el indice especificado'

#                   0     ,  1,   2  ,    3     <-- indices
lista2 = list(["Cocholate", 21, 34.65, "Mundo"])

print("""\nLa lista que usaremos es:
{}
""".format(lista2))

resultado_insert = lista2.insert(2, "Alexis")
resultado_insert = lista2.insert(5, "Valeria")
resultado_insert = lista2.insert(0, 156)

print("La lista nueva que tenemos al usar el metodo insert es:\n{}".format(lista2))
print("==================================================================")

#========================================================================================
'Metodo extend'
'Este metodo extend() va a agregar VARIOS elementos a la lista'

lista3 = list(["Cocholate", 21, 34.65, "Mundo"])

print("""\nLa lista que usaremos es:
{}
""".format(lista3))

resultado_extend = lista3.extend(["joya", 34, "kilates", True,[1, 2]])

print("La nueva lista con todos los nuevos elementos agregador por extend es:\n{}".format(lista3))
print("==================================================================")

#========================================================================================
'Metodo pop'
'este metodo pop() va a a eliminar un elemento de la lista segun el indice que le especifiquemos'

lista4 = list(["Cocholate", 21, 34.65, "Mundo"])

print("""\nLa lista que usaremos es:
{}
""".format(lista4))

# resultado_pop = lista4.pop(2)
# resultado_pop = lista4.pop(1)
resultado_pop = lista4.pop(-1) #ELIMINA EL ULTIMO ELEMENTO DE LA LISTA Y SUCESIVAMENTE

print("La lista nueva que tenemos despues de borrar el ultimo termino con pop es:\n{}".format(lista4))
print("==================================================================")

#========================================================================================
'Metodo remove'
'Este metodo remove() remueve un elemento de la lista, pero debemos indicarle que elemento queremos eliminar'

lista5 = list(["Cocholate", 21, 34.65, "Mundo"])

print("""\nLa lista que usaremos es:
{}
""".format(lista5))

resultado_remove = lista5.remove(21)

print("La nueva lista que tenemos despues de borrar el elemento 22 es:\n{}".format(lista5))
print("==================================================================")

#========================================================================================
'Metodo clear'
'Este metodo clear() elimina todos los elementosde una lista, nos deja una lista vacia'

lista6 = list(["Cocholate", 21, 34.65, "Mundo"])

print("""\nLa lista que usaremos es:
{}
""".format(lista6))

resultado_clear = lista6.clear()

print(lista6)
print("==================================================================")

#========================================================================================
'Metodo sort'
'Este metodo sort() ordena la lista de forma ascendente o descendente.'
#NOTA: SOLO FUNCIONA SI LA LISTA ES DE PUROS NUMEROS (INT, FLOAT), NO CADENAS

lista7 = [23, 43, 76, 4, 6.6, 8, 10.22, 45, 54, 100, 1, 0,False, True, False]
#NOTA: ACEPTA VALORES BOOLEANOS

print("""\nLa lista que usaremos es:
{}
""".format(lista7))

resultado_sort = lista7.sort() #SU PARAMETRO PREDETERMINADO ES reverse=False
'Siendo true ordenara de manera ascendente (menor a mayor)'

print("La lista ordenada de menor a mayor es:\n{}".format(lista7))

resultado_sort = lista7.sort(reverse=True)
'Siendo false ordenara de manera descendente (mayor a menor)'

print("La lista ordenada de mayor a menor es:\n{}".format(lista7))
print("==================================================================")

#========================================================================================
'Metodo reverse'
'Este metodo reverse() va a invertir los elementos de una lista'

lista8 = [23, 43, 76, 4, 6.6, 8, 10.22, 45, 54, 100, 1, 0,False, True, False]

print("""\nLa lista que usaremos es:
{}
""".format(lista8))

resultado_reverse = lista8.reverse()

print("La lista invertida es:\n{}".format(lista8))

# print(dir(lista))
'''Desempaquetado.
Dar valor a variables de una variable ya creada previamente.
Los valores pueden venir de una tupla'''

'Aqui estamos desempaquetando la tupla con los nombres de alunmnos y los estamos almacenando en variables independientes'
datos = ("Alexis", "Valeria", "Pablo", "Cassey", "Omar", 1000)

alumno1, alumno2, alumno3, alumno4, alumno5, alumnos_total = datos

'Tambien funciona con las listas'

datos_lista = ["Rex", "Raptor", "Triceratops", "Brachiosaurio"]

dino1, dino2, dino3, dino4 = datos_lista

'Tambien funciona en conjuntos'
datos_set = {123, 456, 56, 78.90, 45.100}

num1, num2, num3, num4, num5 = datos_set

'''Tuplas
Otra manera de crear tuplas es mediante la sentencia tuple'''

tupla = tuple(["dato 1", "dato 2", "dato 3"])
print(tupla)

'Otra manera de crear tuplas es solo añadiendo la coma los datos de una variable'
tupla2 = "dato 1", 12, 45.76
print(tupla2)

'tupla de un solo dato'
tupla3 = "dato 1",
print(tupla)

'Las tuplas generalmente se crean para guardar datos de solo lectura'

'''Conjuntos
Se pueden crear conjuntos usando la sentencia set'''
conjunto = set(["Dato 1", 123, 45.76, "dato 2"])
print(conjunto)

'No se pueden guardar listas dentro de un conjunto'
'No se pueden guardar diccionarios dentro de un conjunto'

'Si podemos guardar tuplas dentro de un conjunto'
conjunto2 = set(["Dato 1", 123, 45.76, "dato 2",(34, 56, 78)])
print(conjunto2)

'''No se pueden guardar normalmente conjuntos dentro de un conjunto
Pero si usamos la sentencia frozenset si podriamos'''
conjunto3 = frozenset(["dato1", "dato2"])
conjunto4 = {conjunto3, "dato3"}
print(conjunto4)
#NOTA ESTO HARA QUE TENGAMOS UN CONJUNTO DENTRO DE OTRO CONJUNTO

'TEORIA DE CONJUNTOS'
'Agarar datos de un conjunto crea un subconjunto (conjunto a aparte)'

conjunto_a = {1, 3, 5, 7}
conjunto_b = {1, 3, 7}

'Primer manera de comprobar si es un subconjunto'
resultado = conjunto_b.issubset(conjunto_a)

print("El conjunto b es un subconjunto del conjunto a: {}".format(resultado))

'Segunda manera de comprobar si es un subconjunto'
resultado = conjunto_b <= conjunto_a

print("El conjunto b es un subconjunto del conjunto a: {}".format(resultado))

'Para ver si es un superconjunto'

resultado = conjunto_a.issuperset(conjunto_b)
print("El conjunto a es un superconjunto del conjunto b: {}".format(resultado))

'Otra manera de saber si es un superconjunto'

resultado = conjunto_b > conjunto_a
print("El conjunto b es un superconjunto del conjunto a: {}".format(resultado))

'Para verificar si hay un numero en comun dentro de los conjuntos usaremos el metodo isdisjoint'
resultado = conjunto_b.isdisjoint(conjunto_a)
print("Hay valores que no coincidan en los conjuntos a y b: {}".format(resultado))

conjunto_1 = {1, 3, 5, 7}
conjunto_2 = {2, 4, 6, 8}

resultado = conjunto_2.isdisjoint(conjunto_1)
print("Hay valores que no coincidan en los conjuntos a y b: {}".format(resultado))

#NOTA: TIRARA FALSE SI ENCUENTRA UNA SOLA COINCIDENCIA
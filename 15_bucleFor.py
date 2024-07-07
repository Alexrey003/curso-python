'''Bucle FOR

Iterar: Recorrer elementos

En un for solo se pueden ingresar elementos iterables
Elementos iterables:
- Listas
- Tuplas
- Diccionarios
- Conjuntos
- Cadenas de texto

Almacena en una variable los elementos iterables'''

#Primer ejemplo
dinosaurios = ["Triceratops", "Raptor", "Spinosaurio", "T-Rex", "Diplodocus"]

# for dinosaurio in dinosaurios:

'Que hace este for'
#dinosaurio = "Triceratops" PRIMERA VUELTA
#dinosaurio = "Raptor" SEGUNDA VUELTA
#dinosaurio = "Spinosaurio" TERCERA VUELTA
#dinosaurio = "T-Rex" CUARTA VUELTA
#dinosaurio = "Diplodocus" QUINTA VUELTA
#SEXTA SE ROMPE EL BUCLE

for dino in dinosaurios:
    print("El dinosario en esta vuelta es {}".format(dino))

print("\nEl ultimo valor de la variable dino despues del for es {}".format(dino))
print("==========================================================================")

#=============================================================================================

'Bucle for con numeros'
'+=, -=, *=, /=' #OPERADORES DE ASIGNACION
numeros = (23, 10, 2, 54, 231, 1)

for num in numeros:
    print("El valor orignal es: {}".format(num))
    num *= 2
    print(f"El valor multiplicado por 2 es: {num}\n")
print("==========================================================================")

#=============================================================================================
'''Iterando dos listas
Una manera de iterar dos listas es haciendo uso de fors anidados
O
La otra manera es usando la funcion zip()'''
#NOTA: PARA QUE PODAMOS ITERAR DOS LISTAS AMBAS DEBEN DE CONTENER LOS MISMOS ELEMENTOS
animales = ["Conejo", "Nutria", "Mapache", "Leon", "Gato"]
cantidades = [34, 56, 190, 67, 1]

for animal, cantidad in zip(animales, cantidades):
    print(f"Iterando lista 1, valor actual: {animal}")
    print(f"Iterando lista 2, valor actual: {cantidad}\n")
print("==========================================================================")

#=============================================================================================
'Iterando con funcion range()'
'Delimita un rango de numeros (que nosotros definimos), pero no toma en cuenta el ultimo valor'
#NOTA: LA FUNCION RANGE SOLO ACEPTA ENTEROS

for numero in range(1, 11):
    print(f"El numero actual es {numero}\n")
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

print("==========================================================================")

'Aqui no definimos un primer parámetro y por lo tanto toma como valor 0'
for numero in range(6):
    print(f"El numero actual es {numero}\n")
print("==========================================================================")

#=============================================================================================
new_numbers = [12, 23, 34, 78, 123, 234, 567, 800]

'ESTO SOLO MUESTRA LOS INDICES DE CADA ELEMENTO'
# for number in range(len(new_numbers)):
#     print("El indice del elemento actual es {}".format(number))
#no es una manera optima de hacerlo

print("\n")

'La manera optima de hacerlo es en base a la funcion enumerate()'
for enum_num in enumerate(new_numbers):
    print("El valor actual con su indice es: {}".format(enum_num))

print("\nManera no optima de desempaquetar la tulpa anterior")


'Aqui desempaquetamos la tupla previamente creada, pero de una manera no optima'
for indi in enumerate(new_numbers):
    indice = indi[0]
    valor = indi[1]
    print(f"El indice es {indice} y su valor es {valor}")

print("\nManera optima")

'Manera optima de lo anterior'
for index, value in enumerate(new_numbers):
    print(f"El indice es: {index} y su valor es {value}")
print("==========================================================================")

#=============================================================================================
'else junto a for'
dinosaurios = ["Triceratops", "Raptor", "Spinosaurio", "T-Rex", "Diplodocus", "Pteranodon"]
numeros = [23, 10, 2, 54, 231, 1, 24]

for numero in numeros:
    print(f"Ejecutando el bucle actual, valor : {numero}")
else:
    print("El bucle ha terminado")

'Todo esto se puede hacer tanto con tuplas, listas y conjuntos, pero los conjuntos no podran recorrer numeros de la forma optima antes vista'
#LOS CONJUNTOS NO MANEJAN INDICES
print("==========================================================================")

#=============================================================================================
'Iterando un diccionario'

diccionario = {
    "Procesador" : '5600G',
    "Memoria RAM" : '16 GB',
    "Almacenamiento" : '2 TB',
    "Gabinete" : 'Corsair Icue',
    "Periferico 1" : 'Corsair Kgb60 pro'
}

'Iterar las llaves de un diccionario'
for key in diccionario:
    print("La llave es: {}".format(key))

print("\n")

'Iterar los valores del diccionario'
for value in diccionario.items():
    print("La tupla creada a base del diccionario es: {}".format(value))

print("\n")

'Iterando las llaves y sus valores'
'Manero no optima'
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f"La llave es {key} y el valor es {value}")

print("\n")

'Manera optima'
for index, data in diccionario.items():
    print("La llave es: {} Y el valor es: {}".format(index, data))
print("==========================================================================")

#=============================================================================================
'Mas iteraciones'

frutas = ["Manzana", "Piña", "Pera", "Kiwi", "Papaya", "Melón"]

print("Estas son las frutas que tengo:")
for fruta in frutas:
    print(f"- {fruta}")

'Esto va a ser para saltar un elemento del iterable'
for fruit in frutas:
    if (fruit == 'Pera'):
        continue
    print("Me comi una {}".format(fruit))

print("\n")

'Esto va a ser que se termine el bucle'
for fruit in frutas:
    if (fruit == 'Kiwi'):
        break
    print("Me comi una {}".format(fruit))
print("==========================================================================")

#=============================================================================================
'Iterar una cadena de texto'

cadena = "Me gusta el cocholate"

for caracter in cadena:
    print(f"El caracter es: {caracter}")
print("==========================================================================")

#=============================================================================================
'Iteracion en una sola linea de codigo'

numeros = [2, 4, 6, 8, 10, 12]

numeros_duplicados = [num * 2 for num in numeros]

print("Los numeros duplicados son:\n{}".format(numeros_duplicados))

print("\n")

for individual in numeros_duplicados:
    print("El valor es : {}".format(individual))
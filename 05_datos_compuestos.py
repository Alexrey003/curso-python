123, 'texto', 1324.123, True #Datos simples

'LISTAS'
'Para poder definir una lista podemos hacer uso de []'

lista = ["Alexis", 'Valeria', 21, 20, True, False]

print(lista)
print("\n")

'Cada lista va manejada por indices comenzando desde el 0'
'      0    ,     1   ,  2,  3,   4,    5'
# ["Alexis", 'Valeria', 21, 20, True, False]
'Podemos mandar a imprimir/llamar los datos en base a sus indices'

print(lista [1]) #Imprime dato Valeria
print(lista [3]) #Imprime dato 20
print(lista [0]) #Imprime dato Alexis
print("\n")

'Podemos imprimir distintos rangos de indices'
                #0 , 1 ,  2  ,   3  ,  4   ,    5   ,   6 ,   7  ,   8   ,    9    ,  10
lista_grande = [213, 23, True, False, 'asd', 123.123, True, False, 'asdj', '123123','asd']
'No se imprime el ultimo indice'
print(lista_grande [4:8])
print("\n")

'Otra manera de definir una lista es usando la palabra reservada list'
datos = 123, 'texto', 1324.123, True
lista_datos = list(datos)
print(lista_datos)
print("\n")

'Podemos modificar los datos de una lista'
persona1 = ['Valeria', 19, 1.73, False, 'Extrovertida']
print(persona1)
persona1[1] = 22
print(persona1)
print("\n")
#=================================================================================================================
'El otro dato compuesto con el que contamos son las tuplas, se definen por ()'
tupla = ("Sergio", 32, 1.80, True)
print(tupla)
print("\n")

'Las tuplas no se pueden modificar'
# tupla[3] = 123

'Lo mismo que con las listas podemos llamar a imprimir sus diferentes indices'
persona2 = ('Alexis', 21, 1.75, True)
'Para llamar al indice se usan corchetes no parentesis'
print(persona2 [1])
print("\n")

'Otra manera de definir una tupla va a ser con la palabra reservada tuple'
datos_tupla = 123, 123, 34.343, '234nd', 183
tupla_datos = tuple(datos_tupla)
print(tupla_datos)
print("\n")
#=================================================================================================================
'El otro tipo de dato compuesto que tenemos en python son los conjuntos se van a definir con {}'
conjunto = {'Tambores', 'Guitarras', 23}
print(conjunto)
print("\n")

'No podemos modificarlos, pero si reedefinirlos'
conjunto = {'Tortugas', 'patitos', 21}
print(conjunto)
print("\n")

'No vamos a poder acceder por indices y no nos permitira repetir valores'
conjunto = {1, 1, 1, 1, 1}
print(conjunto) #Esto solo imprimira el valor 1 ya que nota que se repite dicho valor
print("\n")

'Otra manera de definir un conjunto el mediante la palabra reservada set'
datos_conjunto = 1, 2, 3, 4, 5, 6, 7 ,8, 9, 10
conjunto_datos = set(datos_conjunto)
print(conjunto_datos)
print("\n")
#=================================================================================================================
''''El ultimo tipo de dato compuesto que tenemos son los diccionarios, estos al igual que los conjuntos se van
a definir por {}'''

diccionario = {
    'Procesador' : 'Ryzen 5 5600g',
    'RAM' : '16GB',
    'Almacenamiento' : "2TB"
}

print(diccionario)
print("\n")
'Cada conjunto cuenta con su palabra clave (a la izquierda) y su respectivo valor (a la derecha)'

'Podemos mandar a imprimir un valor mediante su palabra clave'
print(diccionario ['Procesador'])

#====================================================================================================================
'Podemos meter distintos datos compuestos dentro de otro dato compuesto'

lista1 = [1, 2, 3, 4, 5, 6]
lista2 = [7, 8, 9, 10, 11]
lista_compuesta = [lista1, lista2]
print(lista_compuesta)

tupla_compuesta = (123, 123 , lista_compuesta)
print(tupla_compuesta)

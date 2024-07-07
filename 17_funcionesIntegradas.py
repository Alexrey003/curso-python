'''Funciones integradas (Build-in)

Estructura de una funcion:
nombreFuncion(objeto)

print()
input()
len()

Dos tipos de funciones:
- Creadas por python (Build-in)
- Creados por nosotros
'''

#Encontrando el numero mayor de una lista
numeros = [4, 7, 2, 9, 10]
print(max(numeros))

#Encontrando el numero menor de un iterable
numeros = [4, 7, 2, 9, 10]
print(min(numeros))

#redondeando a seis decimales
numero = round(12.3567326)
print(numero)

numero = round(12.3567326, 2)
print(numero)

#devuelve True si todos los valores son verdaderos
resultado_all = all([23, "True", [123,423]])
print(resultado_all)
'Las listas son False cuando son vacias'
'None tambien es falso y el numero 0'

#Suma todos los valores de un iterable
resultado_sum = sum([1, 2, 3, 4, 5])
print(resultado_sum)
#NOTA: ESTO SOLO SUMA NUMEROS


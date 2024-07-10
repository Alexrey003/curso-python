'OPERADORES ARITMETICOS'

'Tipos de operadores'

'Operador Suma "+"'
'Operador Resta "-"'
'Operador Multiplicacion/Producto "*"'
'Operador Division "/"'
'Operador Modulo/Resto "%"' #NOTA: ESTE OPERADOR NO DEVUELVE PORCENTAJES SOLO DEVUELVE RESTO
'Operador Exponente/Potencia "**"'
'Operador Division baja "//"' #NOTA: ESTE OPERADOR VA A DEVOLVER EL ENTERO DE LA DIVISION

#EJEMPLOS

#Declaracion e inicializacion de variables
valor1 = 21
valor2 = 20

#Operador suma +
suma = valor1 + valor2 + 34

print("El resultado de la suma es: {}".format(suma))

#Operador resta -
resta = valor2 - valor1 - 10 - suma

print("El resultado de la resta es: {}".format(resta))

#Operador Multiplicacón *
multi = valor1 * valor2 * 2

print("El resultado de la multiplicacion es: {}".format(multi))

#Operador Division /
div = valor2 / 2 #Siempre devuelven un valor flotante

print("El resultado de la division es: {}".format(div))

#Operador Resto/Modulo %
resto = valor1 % 2

print("El residuo de dividir 21/2 es: {}".format(resto))

#Operador Potencia/Exponente **
exp = valor1 ** 3

print("El residuo de dividir 21/2 es: {}".format(exp))

#Operador Division baja //
div_baja = valor1 // 3 #Va a devolver un valor entero


print("El residuo de dividir 21/2 es: {}".format(div_baja))

'FUNCION TYPE()'
'''Esta funcion nos indica que tipo de dato estamos recibiendo'''

print("")
print("Tipo de dato:")

texto = "Hola"

print(type(div_baja))
print(type(div))
print(type(exp))
print(type(texto))


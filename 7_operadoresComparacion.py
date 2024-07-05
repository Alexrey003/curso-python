'OPERADOR DE COMPARACIÓN'

'Estos operadores comparan dos expresiones y nos devolveran un valor de tipo booleano.'
#Bool : True o False

'TIPOS DE OPERADORES'

'Operador Igual que... "=="'
'Operador Diferente que... "!="'
'Operador Menor que... "<"'
'Operador Menor-igual que... "<="'
'Operador Mayor que... ">"'
'Operador Mayor-igual que... ">="'

#Ejemplos:
#Declaracion e inicializacion de variables
valor_1 = 69
valor_2 = 24
valor_3 = 13
valor_4 = 4

#Comparaciones
equal = valor_1 == valor_3

'Esto de devolvera un False ya que no son iguales'
print("Los valores son iguales: {}".format(equal))

diff = valor_3 != valor_3

'Esto te devolvera un False ya que no son diferentes'
print("Los valores son diferentes: {}".format(diff))

minor = valor_4 < valor_2


print("El valor es menor: {}".format(minor))

minor_equal = valor_3 <= valor_2


print("El valor es menor-igual que: {}".format(minor_equal))

mayor = valor_1 > valor_3


print("El valor es mayor: {}".format(mayor))

mayor_equal = valor_4 >= valor_4


print("El valor es mayor-igual que: {}".format(mayor_equal))


'ESTAS COMPARACIONES TAMBIEN SE PUEDEN HACER CON STRINGS'

# USER_SAVE = 12

user_save = "Valeria Rivero"
user_written = "vALERIA Rivera"

print("La comparacion entre usuarios es: {}".format(user_written == user_save))
# print(id(User_Save))
# print(id(user_save))
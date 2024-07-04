"""Podemos concatenar diferentes tipos de dato en python, a lo que se refiere que podemos unir
digamos cadenas de texto con otra cadena de texto, o con un numero, etc"""

"""Los datos mas faciles de concatenar son los de tipo str que simplemente agregando un "+" podemos concatenar dos cadenas de texto.
Hay que tener en cuenta que en una cadena de texto todo es un caracter, incluidos los espacios, entonces si queremos concatener una frase
seguida de otra hay que recordar agregar el espacio despues de la primer cadena"""

#Definiendo variables de tipo texto
bienvenida = "Hola buena tarda "
nombre = "Valeria"
#Guardando la concatenacion en una variable
frase = bienvenida + nombre
#Imprimiendo en pantalla la concatenacion
print(frase)

"""Para poder concatenar diferentes tipos de datos a las cadenas de texto para poder agrupar la informacion
no basta con poner un solo "+" ya que al querer concatenar un entero digamos, el + lo tomara como operador aritmetico"""

#Creacion de las variables
num = 20
nombre = "Alexis"

'Al ejecutar esta linea nos tirara una excepcion por lo que dijimos anteriormente ya que queremos unir un numero con un texto'
# print(bienvenida + nombre + num + "años de edad") ERROR

'La manera de evitar esto es con la creacion de un f-string, que nos dara la oportunidad de añadir diferentes datos a una cadena de texto'
#Creando un f-string para evitar la excepcion
#PRIMER MANERA DE CONCATENAR
frase = f"Hola Dios griego {nombre}, tu edad es de {num} años, y cumples {21} años este año"
#Imprimiendo en pantalla el resultado
print(frase)

"""Existe otra manera y es haciendo uso de un metodo de texto que es el ".format()" que nos permitira crear un f-string"""
#SEGUNDA MANERA
#Declarando variables
nombre_com = "Samuel de Luque"
edad = 34
adjetivo = "guapisimo"
#Concatenando diferentes datos usando el metodo .format()
#Mandando a imprimir en patanlla
print("Hola {}, {} tu edad es de {} años, que viejo".format(adjetivo, nombre_com, edad))
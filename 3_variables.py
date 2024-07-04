"""Las variables en general en cualquier lenguaje de programacion son objetos en donde nosotros podremos
almacenar los distintos tipos de datos que queramos ya sean str, int, float, bool, listas, tuplas o diccionarios
esto en caso de Python, podria variar los datos en otros lenguajes
"""

#CREANDO LAS VARIABLES 
'Una variable debe seguir la estructura "nombre" = "dato"'
#Varaibles de tipo int
variable1 = 10 
variable2 = 30 

'A su vez podemos crear variables que contengan otras variables'
#Variable sumando las primeras dos variables (10 + 30)
resultado = variable1 + variable2
#Imprimiendo variable resultado
print(resultado)

'Como dijimos las variables pueden almacenar cualquier tipo de dato'
texto = "Hola" #DATO STR
numero = 69 #DATO INT
flotante = 10.56 #DATO FLOAT
booleano = True #DATO BOOL

'Las variables como su nombre lo indica varian durante la ejecucion de nuestro programa, pueden cambiar de dato'
#Reedefiniendo las variables
resultado = numero + flotante #Cambiando la suma
#Imprimiendo el resultado
print(resultado)
#Cambiando el dato y la suma
resultado = 100 + 1
#Imprimiendo el nuevo resultado
print(resultado)

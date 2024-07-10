'''Modulos

Cualquier archivo que tenga la extension .py es un módulo

- llamar a otro modulo desde otra modulo
- formar paquetes
- mmodulos con diferentes funciones

Tres tipos de de modulos:
1. Python Modules: Modulos que ya vienen integrados en la libreria estandar de python
2. Third-Party Modules: Modulos creados por terceros subidos al internet.
3. Own Modules: Modulos creados por nosotros mismos.
'''

#Importando modulo funciones
# import funciones

'A la hora de trabajar en este caso con las funciones del modulo las trabajaremos como metodos'
# saludo = funciones.saludo("Valeria")
# print(saludo)

'Al importar modulos propios se crea __pycache__ que mejora la velocidad de importacion e ejecucion'

'Simplificando nombre modulo'
# import funciones as funct #Es como si lo guardasemos en una variable

# saludo = funct.saludo("Valeria")
# suma = funct.suma(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# despedida = funct.despedida("Valeria")

# print(saludo)
# print(suma)
# print(despedida)

'Importando una sola funcion/metodo del modulo funciones'
# from funciones import saludo_mejorado, contrasenia #Al hacer esto pasan a trabajarse como funciones en vez de metodos

# saludo_mejorado()
# print(contrasenia())


'Podemos tambien aplicar un dir a nuestro modulo'
# import funciones

# print(dir(funciones))
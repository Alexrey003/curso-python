import os #Lo usaremos para limpiar la pantalla

'''Excepciones

Evento: Todo lo que ocurre dentro de python'''

#Ejemplo de evento
# nombre = input('Ingresa tu nombre:')

# print(nombre)

'''Excepcion: Ocurren en la ejecución del codigo, interrumpir el flujo de ejecucion del programa.
Para ello esta el manejo de excepciones'''

#Forzando una excepcion
# def sumar_dos():
#     a = input('Numero 1: ')
#     b = input('Numero 2: ')
#     resultado = int(a) + int(b)
#     return resultado

# print(sumar_dos())
'ESTO DARA VALUEERROR'

#Manejando la excepcion del programa
'Vamos a tener dos palabras reservadas para manejar las excepciones: try y except'
# def sumar_dos():
#     a = input('Numero 1: ')
#     b = input('Numero 2: ')
#     try:
#         resultado = int(a) + int(b)
#     except:
#         print('Error: Debe ingresar valores numericos')
#     return resultado

# print(sumar_dos())
'ESTO DARA UNBOUNDLOCALERROR ya que resultado no tiene ningun valor asociado para retornar'

#Manejando la segunda excepcion
# def sumar_dos():
#     while True:
#         a = input('Numero 1: ')
#         b = input('Numero 2: ')
#         try:
#             resultado = int(a) + int(b)
#         except:
#             os.system('cls')
#             print('Error: Debe ingresar valores numericos')
#         else:
#             break
#         # finally:
#         #     print('Este codigo se ejecuta siempre, independientemente de si hubo una excepcion o no') ESTA ES UNA SENTENCIA RARA DE USAR
#     return resultado

# print(sumar_dos())

'Podemos acceder a todas las excepciones usando except Exception (es un objeto de una clase)'
# def sumar_dos():
#     while True:
#         a = input('Numero 1: ')
#         b = input('Numero 2: ')
#         try:
#             resultado = int(a) + int(b)
#         except Exception as e:
#             os.system('cls')
#             print(f'ERROR: {type(e).__name__}: {e}') #Aqui mostramos en una sola linea la excepcion que ocurre
#         else:
#             break
#         # finally:
#         #     print('Este codigo se ejecuta siempre, independientemente de si hubo una excepcion o no') ESTA ES UNA SENTENCIA RARA DE USAR
#     return resultado

# print(sumar_dos())

'Usando la palabra reservada raise podemos llamar a cualquier excepcion'

# raise ZeroDivisionError('Dividiste entre 0')

'Aqui creamos nuestra propia excepcion'
class MiExcepcion(Exception):
    def __init__(self, error_message):
        print(f"El error es {error_message}")

try:
    raise MiExcepcion('Error mio')
except:
    print('Esta fue mi excepcion')

raise MiExcepcion("Mi error perdon")

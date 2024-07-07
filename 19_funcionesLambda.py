'''Funciones lamda

Las funciuones lambda reemplazan estas funciones
def multiplicacion(x):
    return x * 2

Estructura:
nombre_variable = lambda parametro : operacion'''

multiplicacion = lambda x : x * 2
print(multiplicacion(2))

'No son aptar para cuando tenemos que realizar mas instrucciones'

'Funcion filter'
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

'Funcion no lambda para comprobar si los numeros son pares'
def es_par(num):
    if(num % 2 == 0):
        return True
    
numeros_pares = filter(es_par, numeros)

print(list(numeros_pares))

'Con funcion lambda'

numeros_pares = filter(lambda numero : numero % 2 == 0, numeros)
print(list(numeros_pares))

'''Funciones propias

Para crear una funcion propia usaremos la palabra reservada def

Estructura:
def nombre_funcion(Parametros):
    Codigo de la funcion'''

#POR NORMA OFICIAL LAS FUNCIONES Y MÉTODOS SE ESCRIBEN EN CAMEL CASE
def saludar():
    print("Hola que tal")

saludar()

'Funcion con parámetros'
def despedida(nombre, apellido):
    print(f"Adios {nombre} {apellido}, que te vaya bien")

despedida("Alexis", "Reynoso")

'Funcion para sumar dos valores'
def suma(a, b, c):
    d = a + b + c
    print(f"El resultado de tu suma es: {d}")

suma(1, 2, 4)

'Funcion con if'
def saludo(nombre, sexo):
    sexo = sexo.lower()
    if (sexo == 'mujer'):
        adjetivo = 'guapa'
    elif (sexo == 'hombre'):
        adjetivo = 'guapo'
    else:
        adjetivo = 'especial'
    
    print(f"Hola {nombre}, que tal estas {adjetivo}")

saludo("Alexis", "hombre")
saludo("Valeria", "mujer")
saludo("Jaimito", "elle")

'Sentencia return'

def generador_contraseña(num):
    chars = """AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz@_."""
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    c4 = num
    c5 = num - 3
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{chars[c4]}{chars[c5]}{num * 3}"
    return contraseña

contra = generador_contraseña(453)
frase = f"Tu contraseña nueva es:{contra}"
print(frase)

'Parámetro args(*parametro)'
def suma(a,b):
    return a + b

resultado = suma(20, 23)
print(resultado)


'Manera no optima de sumar más valores a esta funcion'
def suma(lista):
    numeros_sumados = 0
    for numero in lista:
        numeros_sumados = numeros_sumados + numero
    return numeros_sumados

resultado = suma([20, 23, 12, 3, 43, 65, 12])
print(resultado)

'Usando parámetro args'
def suma(*numeros):
    return sum(numeros)

resultado = suma(123, 23, 345, 56, 87, 90, 124, 34, 123, 1,31 ,31,2, 312)
print(resultado)

'El parametro args siempre debe ser tu ultimo parametro'
def suma(nombre,*numeros):
    return f"{nombre} la suma de tus numeros es {sum(numeros)}"

resultado = suma("Sergio", 23, 10, 11, 12)
print(resultado)


'Las funciones que declares con parámetros, debes de respetar el orden en el que ingresas los valores de dichos parametros'
def saludo(nombre, apellido, adjetivo):
    return f"Hola {nombre} {apellido}, eres muy {adjetivo}"

frase = saludo("Moles", "guapo", "Valeria")
print(frase)

'Pero podemos forzar los parametros mediante key arguments'
def saludo(nombre, apellido, adjetivo):
    return f"Hola {nombre} {apellido}, eres muy {adjetivo}"

frase = saludo(adjetivo = "guapo", apellido = "Moles", nombre = "Sergio")
print(frase)

'Podemos dar valor a un parametro desde la propia funcion'
def saludo(nombre, apellido, adjetivo = "tonto"):
    return f"Hola {nombre} {apellido}, eres muy {adjetivo}"

frase = saludo(apellido = "Moles", nombre = "Sergio")
print(frase)
'podemos reedefinir los valores ya que son variables'
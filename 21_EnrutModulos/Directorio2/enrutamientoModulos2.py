#Creando una funcion que nos devuelva los numeros primos
#entre el 0 y el argumnento que pasamos

#Funcion que verifica si un num es primo
def es_num_primo(num):
    #verificamos que el numero pasado no pueda dividirse por ningun numero entre 2 y ese mismo numero -1
    for i in range(2, num - 1):
        #Si es divisible por alguno retornamos False y termina el bucle
        if num % i == 0: return False
    #Si termina el bucle, significa que no fue divisible entonces es primo
    return True

#Funcion que retorne una lista con todos los primos
def primos_hasta(num):
    #Creamos la lista
    primos = []
    for i in range(3, num + 1):
        #Verificamos si el valor es primo
        resultado = es_num_primo(i)
        #En caso de que sea lo agregamos a la lista
        if resultado == True: primos.append(i)
    #Devolvemos la lista
    return primos

#Creamos resultado llamando a la funcion y lo mostramos
# resultado = primos_hasta(98)
# print(resultado)ta(98)
# print(resultado)


def saludo(name):
    return f"Hola {name}, me gustan los cocholates y a ti?"

def suma(*num):
    return sum(num)

def despedida(name):
    return f"Adiós {name}, espero que hayas disfrutado de los cocholates y a ti también."

def saludo_mejorado():
    nombre = input("Ingrese su nombre: ")
    print(saludo(nombre))
    print(f"La suma de los primeros 10 números naturales es: {sum(range(1, 11))}")
    print(despedida(nombre))

def contrasenia():
    contrasenia = input("Ingrese una contraseña: ")
    if len(contrasenia) >= 8 and any(char.isdigit() for char in contrasenia) and any(char.isupper() for char in contrasenia) and any(char.islower() for char in contrasenia):
        return f"Tu contraseña es segura"
    else:
        return f"Tu contraseña es insegura"
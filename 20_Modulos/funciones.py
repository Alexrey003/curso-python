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
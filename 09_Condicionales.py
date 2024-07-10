'CONDICIONALES (IF, ELSE, ELIF)'

'Para este punto vamos a empezar a trabajar con inputs'

# edad = int(input("Ingresa tu edad: "))

# if (edad >= 18):
#     print("Eres mayor de edad maquinola")
# else:
#     print("Eres menor de edad muquiento")

# password_save = "meGustanloscohcholATES"
# password_written = "MegustanLOScocholateS"

# if (password_written == password_save):
#     print("Contraseña correcta.")
# else:
#     print("CONTRASEÑA INCORRECTA.viene el FBI PERRO")

# ingreso_mensual = 8500

# if (ingreso_mensual > 1000):
#     print("Tienes un salario mejor que el promedio de latam")
# elif (ingreso_mensual > 10000):
#     print("Tienes un buen salario mundialmente")
# else:
#     print("No tienes un buen salario. \nSal a buscar un trabajo vago")

print("Verificadora de edad")
edad = int(input("Ingresa tu edad: "))

if (edad >= 18):
    print("Tienes la mayoria de edad para manejar.")
    
    carnet = input("Si cuentas con carnet de conducir ingresa si, en caso contrario ingresa no: ").lower()
    
    if (carnet == 'si'):
        print("Entonces eres mayor de edad y cuentas con carnet de conducir. Maneja con cuidado")
    elif (carnet == 'no'):
        print("No cuentas con tu carnet de conducir, realiza el examen para conseguirlo")
    else:
        print("Ingresa un dato valido porfavor")
        
elif (edad < 18):
    print("No eres mayor de edad vuelve cuando lo seas")
else:
    print("Ingresa un dato válido")

print("AQUI VA EL RESTO DEL CODIGO")
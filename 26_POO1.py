'''Programacion orientada a objetos (P.O.O)

Traslada la naturaleza de los objetos de la vida real al codigo de programacion
Es decir,los objetois tienes un estado, comportamiento, propiedaes, etc.

Veámoslo con él objeto coche:
1.	¿Cuál es el estado de un coche?: Un coche puede estar parado, circulando, aparcado, etc.

2.	¿Qué propiedades tiene un coche?: Un coche tiene color, peso, tamaño, etc.

3.	¿Qué comportamientos tiene un coche?: Un coche puede arrancar, frenar, acelerar, girar, etc.

Otro objeto un celular:
1.	¿Cuál es el estado de un celular?: Un celular puede estar apagado, encendido, etc.

2.	¿Qué propiedades tiene un celular?: Un celular tiene color, marca, tamaño, componentes, etc.

3.	¿Qué comportamientos tiene un celular?: Puede realizar llamadas, enviar mensajes, mostrar notis, etc.

Ventajas:
- Modularizacion (Podemos dividir nuestro codigo en diferentes partes)
- Codigo reutilizable (Herencia)
- Trata exepciones
- Encapsulamiento

Lenguaje/jerga comun del POO:
- clase
- objetos
- instancias de clase
- modularizacion
- encapsulamiento
- herencia
- polimorfismo

Veremos todo esto en ejemplo de una PC

Clase: Es un molde/plantilla/modelo donde pondremos las caracteristicas comunes de un grupo de objetos

La clase PC, alcamenda las propiedades, ya sea medidas del gabinete, marca componentes, precio, perifericos, ventiladores, etc

Objeto: Es una instancia de una clase, que puede tener diferentes caracteristicas propias

Instancia de clase: Es un objeto perteneciente a la clase

Modularizacion: Es dividir nuestro programa en diferentes partes, cada modulo va a trabajar de una manera independiente
Si un modulo falla no afecta a los demas y podemos llamar a un modulo dentro de otro

Encapsulamiento: Es ocultar los detalles de implementacion de un objeto y solo permitir que el objeto mismo interactue con el

Para conectar clases entre si se hace uso de los metodos de acceso, al hacer esto solo tendran acceso a ciertas caracteres
de cada una de las clases

Para poder acceder a propiedades y comportamientos de un objeto, usaremos la nomenclatura del punto o sintaxis de métodos

Objeto Consola:
•	Accedemos a propiedades (atributos o variables):
    o	Consola.marca = “Sony”;
    o	Consola.Modelo = “PS5”;
    o	Consola.color = “Negro”;
    o	Consola.peso = 5000;
•	Accedemos a comportamientos (métodos o funciones):
    o	Consola.enciende();
    o	Consola.apaga();
    o	Consola.lectura_disco();
    o	Consola.Acceso_juego();
'''
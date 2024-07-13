class PC():
#Atributos de una PC
#Propiedades iniciales de la clase para cada objeto
#EL ENCAPSULAMIENTO ES OPCIONAL VARIA SEGUN LA PROPIEDAD
    def __init__(self):
        self.__ancho_gabinete = 280
        self.__alto_gabinete = 480
        self.__largo_gabinete = 430
        self.ventiladores_gabinete = 7
        self.color_gabinete = "Negro"
        self.power = False
#Metodos de una PC
#Pasamos un segundo parámetro a este metodo
    def encender(self, encendemos):
        self.power = encendemos
        #objeto.power = encendemos
        if (self.power):
            return "La pc esta encendida"
        else:
            return "La pc esta apagada"
    def especificaciones(self):
        print(f"El ancho del gabinete es de {self.__ancho_gabinete}mm")
        print(f"La altura del gabinete es de {self.__alto_gabinete}mm")
        print(f"El largo del gabinete es de {self.__largo_gabinete}mm")
        print(f"El gabinete cuenta con {self.ventiladores_gabinete} ventiladores")
        print(f"El color del gabinete es {self.color_gabinete}")


#Instanciando una PC
valeria_pc = PC()
alexis_pc = PC()

#Impresiones de propiedades de la pc1
print("-------Especificaciones gabinete--------")
valeria_pc.especificaciones()

print("--------Estado de la PC---------------")
print(valeria_pc.encender(True))

#Impresiones de propiedades de la pc2
print("-------Especificaciones gabinete--------")
alexis_pc.especificaciones()

print("--------Estado de la PC---------------")
print(alexis_pc.encender(False))

'''Teniendo la propiedades como las tenemos ahorita mismo:
    def __init__(self):
        self.ancho_gabinete = 280
        self.alto_gabinete = 480
        self.largo_gabinete = 430
        self.ventiladores_gabinete = 7
        self.color_gabinete = "Negro"
        self.power = False'''

#Podemos modificar las propiedades si no se tiene encapsulamiento
# valeria_pc.__alto_gabinete = 123
# valeria_pc.especificaciones()

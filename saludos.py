from pyknow import *
class Datos(KnowledgeEngine):
    @DefFacts()
    def principal(self):
        yield Fact(inicio="saludo")

 

    @Rule(Fact(inicio='saludo'),NOT(Fact(nombre=W())))
    def ask_name(self):
        self.declare(Fact(nombre=input("¿Como te llamas? ")))
        
    @Rule(Fact(inicio='saludo'),NOT(Fact(profesion=W())),Fact(nombre=W()))
    def ask_location(self):
        self.declare(Fact(profesion=input("¿Cual es tu profesion? ")))
        
    @Rule(Fact(inicio='saludo'),Fact(nombre="nombre" << W()),Fact(profesion="profesion" << W()))
    def greet(self, nombre, profesion):
        print("Hola %s!  %s" % (profesion, nombre))

    @Rule(Fact(nombre=L("Josue"))& Fact(profesion=L("docente")))
    def josue_fcc(self):
        print("Bienvenido docente Josue ")

    @Rule(Fact(inicio='saludo'),NOT(Fact(mascota=W())))
    def mascota(self):
        self.declare(Fact(mascota= input("Tipo de mascosa: "), edad= input("Edad de mascota: ")))

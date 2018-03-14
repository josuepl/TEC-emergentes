from pyknow import *

class pax(Fact):
    pass

def enfermedad():
    a=input("Ingresa tu enfermedad")
    return a
    pass

def sintoma():
    return input("Ingresa tu sintoma")
    pass

def salir():
    return input("ADIOS")
    pass

class doc(KnowledgeEngine):
    
    @DefFacts()
    def principal(self):
        yield Fact(inicio="inicio")
        pass

    @Rule(Fact(inicio=L("inicio")),~pax(nombre=W()))
    def p_nm(self):
        self.declare(pax(nombre=input("Nombre del paciente: ")))
        pass

    @Rule(pax(nombre='nombre'<< W()))
    def mev(self,nombre):
        print("Opciones\n1.- Define enfermedad\n2.- Define sintoma\n3.- salir")
        opciones = { '1': enfermedad, '2': sintoma, '3': salir}
        seleccion = input('Elige una opción: ')
        try:
            resultado = opciones[seleccion]()
            print("ress: ", resultado)
            self.declare(pax(nombre=nombre,enfermedad=resultado))
        except:
            print("opcion no valida")
        pass


    

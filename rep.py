from pyknow import *


class Numero(Fact):
    
    pass

class Juegovalores(KnowledgeEngine):
    
    
    @Rule(Numero(valor==6))
    def reprobado(self):
        print("Reprobado")

    @Rule(Numero(valor>6))
    def aprobado(self):
        print("Aprobado")

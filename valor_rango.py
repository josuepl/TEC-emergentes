from pyknow import *
from graphviz import *

class numero(Fact):
    pass

def isint(x):
    return isinstance(x,int)

def operacion(y):
    print("operacion: ", y)
    return y + 8

    
class valores(KnowledgeEngine):
    @Rule(Fact(('y' << P(isint)) & ('y' << P(isint))))
    def camb(self,y):
        print("camb",y)
        self.declare(Fact(operacion(y),y + 1, y + 22))
        
    @Rule(Fact(('y' << P(lambda x: x >= 0)) & ('y' << P(lambda x: x <= 1024))))
    def intert(self,y):
        print("intert",y)
    
       

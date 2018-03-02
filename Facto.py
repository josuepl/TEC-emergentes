from pyknow import *

class Factorial(Fact):
    pass

def isint(x):
    if(x == '4'):
        print("Eel iva es",x)
    return isinstance(x,int)
    
    
class CF(KnowledgeEngine):
    @DefFacts()
    def principal(self):
        yield Fact(main="main")
        
    @Rule(Fact(main="main"))
    def inicia(self):
        self.declare(Factorial((input("Ingresa el valo5r base")),(input("Ingresa el valor base"))))

    
    @Rule(Factorial('x' << P(isint),
                    'y' << P(isint)))
    def factor(self, x, y):
        self.declare(Factorial(x + 1, (x + 1) * y))

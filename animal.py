from pyknow import *
class MyFact(Fact):
    pass

class animal(KnowledgeEngine):
    @Rule(MyFact())  # This is the LHS
    def match_with_every_myfact(self):
        """This rule will match with every instance of `MyFact`."""
       
        pass

    @Rule(Fact('animal', family='felinae'))  # This is the RHS
    def match_with_cats(self):
        """
        Match with every `Fact` which:

          * f[0] == 'animal'
          * f['family'] == 'felinae'

        """
        print("Meow!")

    @DefFacts()
    def needed_data(self):
        yield Fact(tipo="gato")
        yield Fact(tamaño="mediano")
        yield Fact(color="gris")

from abc import *

class Computer(ABC): #Abstract Class and we cant create object of this class.
    @abstractmethod
    def process(self):
        pass
       #pass is used when we do not need to define anything

class Lenovo(Computer):
    def process(self):
        print("Used Abstract Class")
    def execute(self):
        print("Lenovo is running Fast")

class Programmer:
    def Bala(self,Saala):
        Saala.process()

L1 = Lenovo()
#L1.process()
#L1.execute()
Pro = Programmer()
Pro.Bala(L1) #Duck Typing in Abstract Classes.


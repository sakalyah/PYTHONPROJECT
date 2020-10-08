class ABC :
    def __init__(self):
        self.name = "Harish"
        print(self.name)
    def f1(self):
        print("Feature 1")
    def f2(self):
        print("Feature 2")

class PQR(ABC) :  #SIngle Inheritance in Python
    def __init__(self):
        super().__init__()
        self.team = "SRH"
        print(self.team)
    def f3(self):
        print("Feature 3")
    def f4(self):
        print("Feature 4")

A =ABC()
B = PQR()

class P :
    def __init__(self):
        self.name = "RABADA"
        print(self.name)
    def f6(self):
        print("Feature 6")
class Q :
    def __init__(self):
        self.name = "BHUVI"
        print(self.name)
    def f7(self):
        print("Feature 7")

class R(P,Q): #Multiple INheritance
    def __init__(self):
        super().__init__()
        self.name = "DHONI"
        print(self.name)
    def f8(self):
        print("Feature 8")

RR =R()
#In the above code only constructors of P and R classes will be called due to a mechanism called
# Method Resolution Order (MRO)


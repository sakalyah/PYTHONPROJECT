class Bandu:
    def __init__(self,name,c1,c2,c3):
        print("In INIT")
        self.name = name
        self.c1=c1
        self.c2=c2
        self.c3=c3
    def config(self):
        print(self.name+" Details Are :",self.c1,self.c2,self.c3)

A=Bandu("LAMDI","CG","CTS","ZOHO") #Object creation
A.config()

class Bandu1:
    wheels = 5
    def __init__(self):
        self.handle = 1
        self.seat =1
        self.wheels =3
    def specifics(self):
        return self.handle + self.seat + self.wheels

C1 = Bandu1()
C1.seat = 3
C1.handle =2
C1.wheels=4
Bandu1.wheels=4
print(C1.seat,C1.handle,Bandu1.wheels,C1.wheels,C1.specifics())
C2=Bandu1()
C2.seat = 32
C2.handle =10
C2.wheels=8
print(Bandu1.wheels,C2.specifics())





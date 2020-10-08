class ABC :
    def f1(self):
        print("Feature 1")
    def f2(self):
        print("Feature 2")

class PQR(ABC) :  #SIngle Inheritance in Python
    def f3(self):
        print("Feature 3")
    def f4(self):
        print("Feature 4")

A = PQR()
B = ABC()
A.f3()
A.f1()
B.f2()

class DEF(PQR): #MultiLevel Inheritance
    def f5(self):
        print("Feature 5")
#PQR = Child Class , ABC = Super Class

C = DEF()
C.f5()
C.f2()
C.f3()

#HEre DEF = Child class of both PQR and ABC

class P :
    def f6(self):
        print("Feature 6")
class Q :
    def f7(self):
        print("Feature 7")

class R(P,Q): #Multiple INheritance
    def f8(self):
        print("Feature 8")

RR = R()
RR.f6()
RR.f7()
RR.f8()

QQ = Q()
QQ.f7()

PP = P()
PP.f6()

#IN Multiple Inheritance for R class P,Q are Parent/Super classes





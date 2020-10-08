class Harish:
    def __init__(self):
        print("In INIT")
    def config(self):
        print("Harish","CTS","CAPGEMINI")
        x="Harish"
        y=9
        print(type(y),type(x))

A = Harish()#One way of creating Object
A.config()
print(type(A))
B=Harish()
Harish.config(B)#Backend Way of creating an Object
B.config()
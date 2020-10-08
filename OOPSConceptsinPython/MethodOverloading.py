class CSK:
    def sum(self,a=None,b=None,c=None):

        if a!=None and b!=None and c!=None :
            d = a +b + c
            return d
        elif a!=None and b!=None :
            d =a + b
            return d
        else :
            d = a
            return d

csk = CSK()
print(csk.sum(90,89))
print(csk.sum(67,987,456))
print(csk.sum(1000))

def sum(x,y):
    x=int(input('Enter Input of X : '))
    y = int(input('Enter Input of Y : '))
    c = x+y
    d = x-y
    return c,d

#a,b = sum(0,0)#If user is giving inputs we need to pass 0 to the arguments while calling the function
#print(a,b)

def update(x):
    print(id(x))
    x=8
    print(id(x))
    print('x:',x)
def update1(lst):
    print(id(lst))
    lst.append(7800)
    print(id(lst),lst)

lst=[10,25,78,1256]
print(id(lst))
update1(lst)
print(lst)
"""a=10
print(id(a))
update(a)
print('a: ',a)"""

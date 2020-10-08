
a = 10
b=9
def PQ():
    a=5
    x=globals()['a']
    print(x)
    b=70
    y=globals()['b']
    print(y)
    globals()['a']=800
    globals()['b']=1000
PQ()
print(a)
print(b)
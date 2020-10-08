#Changing the behaviour of an existing function during compile itself is done with the help of Decorators
import Calculator as cal
def div(a,b):
    print(a/b)

#res = div(50,25)
#print(res)
#div is a normal function
def smart_div(func):#Decorator
    def inner(a,b):#Inner Function of Decorator
        if(a<b):
            a,b =b,a
            return func(a,b)
    return inner
result = smart_div(div(200,2000))
#result(4,2)

add = cal.add(45,55)
sub = cal.sub(55,50)
div = cal.div(120,45)
mul = cal.mul(45,78)

print(add,sub,div,mul)


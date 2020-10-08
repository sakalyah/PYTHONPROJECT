import functools
def is_even(n):
    return n%2==0

n1 = [2,3,4,5,6,7,8,9,1001,7805]
result = list(filter(is_even,n1))
print(result)

n2=[123,234,456,789,6547]
result2 = list(filter(lambda n:n%2!=0,n2))
print(result2)
result3 = list(map(lambda n:n*3,n2))
print(result3)
result4 = functools.reduce(lambda a,b:a+b,result3)
print(result4)


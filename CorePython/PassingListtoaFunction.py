
def count(lst):
    even=0
    odd=0
    for i in lst:
        if((i%2)==0):
            even = even +1
        else:
            odd= odd+1
    return even,odd
list = [23,24,25,26,27,28,29,30,31]
a,b = count(list)
print(a,b)
print('Even:{} and Odd:{}'.format(a,b))

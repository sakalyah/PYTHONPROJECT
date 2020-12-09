t = [2,45,456,45678,456789]
#print(len(t))
t.append(900)
t.append(9001)
print(t)
def search(lis,number):
    i = 0
    while i < len(lis):
        if lis[i]==number:
            print("Number found at "+i.__str__())
            return True
        i=i+1
    return False

#Using FOR LOOP
a = search(t,90000)
print(a)

g = [23,45,789,456,1234,987]

def searchhh(list,n):
    for a in range(len(list)):
        if list[a]==n:
            print("Number found at "+a.__str__())
            return True
    return False

b = searchhh(g,8987)
print(b)

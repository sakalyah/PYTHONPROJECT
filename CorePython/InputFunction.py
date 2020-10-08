import math
x=int(input('Enter Value of X:'))
print(math.sqrt(x))
#print(math.acos(x)+math.asin(x))
print(math.floor(math.cos(x)))
List1=[]
List2=[]
for a in range(x):
    if a%4==0:
        List1.append(a)
    else:
        List2.append(a)


print('Numbers that are divisible by 4',List1)
print('Numbers that are not divisible by 4',List2)
cars = ['BMW','Buchuku','buchuku buchuku']
print(cars[1])
print(len(cars))
cars.append('Lamdi')
print(cars)
cars.insert(0,'AUDI')
print(cars)
print(cars.index('Lamdi'))
print(cars.pop())
cars.sort()
print(cars)
slice = cars[0:2]
print(slice)
#Number list
I = [0,1,2,2,2,2,12,13]
print(I.count(12))
for n in cars:
    print(n)
    if len(n)==5:
        print("Size is" +n)
    elif  len(n)==4:
        print("Size is " +n)
    else:
        print("No Condition is Matched")
    print("Inside for loop")
print("Outside For loop")
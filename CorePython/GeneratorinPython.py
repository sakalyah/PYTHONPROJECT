def topten1():
    yield  7

values=topten1()
print(values)
print(values.__next__())

def topten2():
    n =2
    while n<=100:
        a = n*n
        yield a
        n = n + 1

val = topten2()
sound =[]
for lamdi in val:
    print(lamdi)
    sound.append(lamdi)

print(sound,len(sound))

#num = [69,70,71,45,56,67]
#it = iter(num)
#print(it.__next__())
#print(next(it))
#print(next(it))
#print(next(it))
#print(next(it))
#for i in num :
    #print(i)
class Iterator:
    def __init__(self,num):
        self.num =num
    def __iter__(self):
        return self
    def __next__(self):

        if self.num <=100:
            val = self.num
            self.num = self.num + 1
            return val
        else :
            raise StopIteration

it = Iterator(10)
for val in it:
    print(val)
